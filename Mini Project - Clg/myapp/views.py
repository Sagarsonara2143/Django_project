from django.shortcuts import render, redirect
from . models import Contact,User
from django.conf import settings
from django.core.mail import send_mail
import random


# Create your views here.

def index(request):
	return render(request,'index.html')


def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			remarks=request.POST['remarks']
			)
		contacts=Contact.objects.all().order_by('-id')[:5]
		msg="Contact Saved Successfully ..!"
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by('-id')[:5]
		return render(request,'contact.html',{'contacts':contacts})

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg = "Email ID is already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					gender=request.POST['gender'],
					address=request.POST['address'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic']
					)
				msg="User Signup Successfully.."
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Passord and confirm password does not matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
		try:
			user = User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				return render(request,'index.html')
			else:
				msg="Invalid Password"
				return render(request,'login.html',{'msg':msg})
				msg= "Email ID not registered"
				return render(request,'login.html',{'msg':msg})
		except:
			msg= "Email not registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		return render(request,'login.html')
	except:
		return render(request,'login.html')

def change_password(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect('logout')
			else:
				msg="New password and confirm password does	not matched"
				return render(request,'change-password.html',{'msg':msg})
		else:
			msg = "Old password does not matched"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')


def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'OTP for forgot password'
			message = 'Hello '+ user.fname +' ! OTP for forgot password is ' + str(otp)
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email,]
			send_mail( subject, message, email_from, recipient_list )
			msg = "OTP Sent Successfully !!"
			return render(request,'verify-otp.html',{'email':user.email,'otp':otp,'msg':msg})
		except:
			msg = "Opps! Email is not registered"
			return render(request,'forgot-password.html',{'msg':msg})
	else:
		return render(request,'forgot-password.html')

def verify_otp(request):
	email=request.POST['email']
	otp=request.POST['otp']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,'new-password.html',{'email':email})
	else:
		msg="Invalid OTP"
		return render(request,'verify-otp.html',{'email':email,'otp':otp,'msg':msg})
	
def new_password(request):
	email=request.POST['email']
	npwd=request.POST['new_password']
	cnpwd=request.POST['cnew_password']
		
	if npwd==cnpwd:
		user=User.objects.get(email=email)
		user.password=npwd
		user.save()
		msg ="Password updated Successfully..!"
		return render(request,'login.html',{'msg':msg})
	else:
		msg = "New password and confirm new password does not matched"
		return render(request,'new-password.html',{'msg':msg})

def profile(request):
	user = User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.gender=request.POST['gender']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		msg="Profile updated Successfully..!!"
		request.session['profile_pic']=user.profile_pic.url
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})

