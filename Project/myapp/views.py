from django.shortcuts import render,redirect
from .models import User


# Create your views here.

def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Id is already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					city=request.POST['city'],
					zipcode=request.POST['zipcode'],
					password=request.POST['password'],
					)
				msg="User Sign Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm password does not matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')


def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				return render(request,'index.html')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not registered"
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
		user=User.objects.gets(email=request.session['email'])
		if user.password==request.POST['old_password']:
			np=request.POST['new_password']
			cnp=request.POST['cnew_password']
			if np==cnp:
				user.password=np
				user.save()
				redirect ('logout') 
			else:
				msg="New Password & confirm New Password does not matched"
				return render(request,'change-password.html',{'msg':msg})	
		else:
			msg="Incorrect Old Password"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')
