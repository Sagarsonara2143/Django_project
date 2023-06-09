from django.shortcuts import render,redirect
from .models import Contact,Customer,Artist
import random
import requests
# Create your views here.

artist=Artist.objects.all()

def index(request):
	artist=Artist.objects.all().order_by('id')[:3]
	artist_all=Artist.objects.all()
	#print(artist)
	return render(request,'index.html',{'artist':artist,'artist_all':artist_all})

def artist_index(request):
	artist=Artist.objects.all()
	print(artist)
	return render(request,'artist-index.html',{'artist':artist})


def about(request):
	artist=Artist.objects.all().order_by('id')[:3]
	artist_all=Artist.objects.all()
	return render(request,'about-us.html',{'artist':artist,'artist_all':artist_all})

def artist_about_us(request):
	return render(request,'artist-about-us.html')


def artist_change_password(request):
	artist=Artist.objects.get(email=request.session['email'])
	if request.method=="POST":
		if artist.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				artist.password=request.POST['new_password']
				artist.save()
				msg="Password changed successfully"
				return redirect('logout') 
			else:
				msg="New Password & confirm New Password does not matched"
				return render(request,'artist-change-password.html',{'msg':msg})	
		else:
			msg="Incorrect Old Password"
			return render(request,'artist-change-password.html',{'msg':msg})
	else:
		return render(request,'artist-change-password.html')

def forgot_password(request):
	artist=Artist.objects.all().order_by('id')[:3]
	if request.method=="POST":
		try:
			artist=Artist.objects.get(mobile=request.POST['mobile'])
			otp = random.randint(1000,9999)
			mobile=artist.mobile

			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"HHHwvpXNR0sUPZOJqgNJc7BZ5hxRYYocAU7DrHnqb4Q81T63G3c9l3pqxtBN","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.text)
			msg="OTP Sent Successfully"
			return render(request,"verify-otp.html",{'msg':msg,'otp':otp,'mobile':mobile})
		except:
			try:
				customer=Customer.objects.get(mobile=request.POST['mobile'])
				otp = random.randint(1000,9999)
				mobile=customer.mobile

				url = "https://www.fast2sms.com/dev/bulkV2"
				querystring = {"authorization":"HHHwvpXNR0sUPZOJqgNJc7BZ5hxRYYocAU7DrHnqb4Q81T63G3c9l3pqxtBN","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
				headers = {'cache-control': "no-cache"}
				response = requests.request("GET", url, headers=headers, params=querystring)
				print(response.text)
				msg="OTP Sent Successfully"
				return render(request,"verify-otp.html",{'msg':msg,'otp':otp,'mobile':mobile})
			except:
				msg="Mobile Number not registered"
				return render(request,"forgot-password.html",{'msg':msg})
	else:
		return render(request,"forgot-password.html",{'artist':artist})

def verify_otp(request):
	artist=Artist.objects.all().order_by('id')[:3]
	otp=request.POST['otp']
	mobile=request.POST['mobile']
	uotp=request.POST['uotp']

	if otp==uotp:
		#print(mobile)
		return render(request,"new-password.html",{'mobile':mobile,'artist':artist})	
	else:
		msg="Invalid OTP Entered"
		return render(request,"verify-otp.html",{'msg':msg,'mobile':mobile,'otp':otp,'artist':artist})

def new_password(request):
	artist=Artist.objects.all().order_by('id')[:3]
	n_pwd=request.POST['new_password']
	cn_pwd=request.POST['cnew_password']
	mobile=request.POST['mobile']
	if n_pwd==cn_pwd:
		print(mobile)
		try:
			artist=Artist.objects.get(mobile=mobile)
			artist.password=n_pwd
			artist.save()
			return redirect('login')
		except: 
			try:
				customer=Customer.objects.get(mobile=mobile)
				customer.password=n_pwd
				customer.save()
				return redirect('login')
			except:
				return render(request,"new-password.html",{'artist':artist})
	else:
		msg="New Password & Confirm New Password does not Matched"
		return render(request,"new-password.html",{'msg':msg,'artist':artist})


def contact(request):
	artist=Artist.objects.all().order_by('id')[:3]
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],		
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			message=request.POST['message']
			)
		msg="Message Sent Successfully"
		return render(request,'contact.html',{'msg':msg,'artist':artist})
	else:
		return render(request,'contact.html',{'artist':artist})

def artist(request):
	artist=Artist.objects.all().order_by('id')[:3]
	artist_all=Artist.objects.all()
	return render(request,'artist.html',{'artist':artist,'artist_all':artist_all})

def login(request):
	artist=Artist.objects.all().order_by('id')[:3]
	if request.method=="POST":
		try:
			artist=Artist.objects.get(email=request.POST['email'])
			if artist.password==request.POST['password']:
				request.session['email']=artist.email
				request.session['fname']=artist.fname
				request.session['profile_pic']=artist.profile_pic.url
				request.session['about']=artist.about
				return redirect("index")
			else:
				msg="Password does not matched"
				return render(request,'login.html',{'msg':msg,'artist':artist})
		except:
			try:
				customer=Customer.objects.get(email=request.POST['email'])
				if customer.password==request.POST['password']:
					request.session['email']=customer.email
					request.session['fname']=customer.fname
					request.session['profile_pic']=customer.profile_pic.url
					request.session['address']=customer.address
					return redirect("index")
				else:
					msg="Password does not matched"
					return render(request,'login.html',{'msg':msg,'artist':artist})
			except:
				msg="Email does not registered"
				return render(request,'login.html',{'msg':msg,'artist':artist})
	else:
		return render(request,'login.html',{'artist':artist})

def signup(request):
	artist=Artist.objects.all().order_by('id')[:3]
	if request.method=="POST":
		try:
			Customer.objects.get(mobile=request.POST['mobile'])
			msg="Mobile Number is already registered"
			return render(request,'signup.html',{'msg':msg,})
		except:
			try:
				Customer.objects.get(email=request.POST['email'])
				msg="Email Id is already registered"
				return render(request,'signup.html',{'msg':msg,'artist':artist})
			except:
				if request.POST['password']==request.POST['cpassword']:
					Customer.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
						)
					msg="Signup Successfully"
					return render(request,'login.html',{'msg':msg,'artist':artist})
				else:
					msg="Password & Confirm password does not match"
					return render(request,'signup.html',{'msg':msg,'artist':artist})
	else:
		return render(request,'signup.html',{'artist':artist})


def signup_artist(request):
	if request.method=="POST":
		try:
			Artist.objects.get(mobile=request.POST['mobile'])
			msg="Mobile Number is already registered"
			return render(request,'signup-artist.html',{'msg':msg,})
		except:
			try:
				Artist.objects.get(email=request.POST['email'])
				msg="Email Id is already registered"
				return render(request,'signup-artist.html',{'msg':msg,})
			except:
				if request.POST['password']==request.POST['cpassword']:
					Artist.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						about=request.POST['about'],
						facebook=request.POST['facebook'],
						instagram=request.POST['instagram'],
						twitter=request.POST['twitter'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
						)
					msg="Signup Successfully"
					return render(request,'login.html',{'msg':msg,})
				else:
					msg="Password & Confirm password does not match"
					return render(request,'signup-artist.html',{'msg':msg,})
	else:
		return render(request,'signup-artist.html')
	

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		del request.session['usertype']
		return redirect('login')
	except:
		return redirect('login')

def profile(request):
	artist=Artist.objects.all().order_by('id')[:3]
	try:
		customer=Customer.objects.get(email=request.session['email'])
		if request.method=="POST":
			customer.fname=request.POST['fname']
			customer.lname=request.POST['lname']
			customer.email=request.POST['email']
			customer.mobile=request.POST['mobile']
			customer.address=request.POST['address']
			try:
				customer.profile_pic=request.FILES['profile_pic']
			except:
				pass
			customer.save()
			request.session['profile_pic']=customer.profile_pic.url
			msg="Profile Updated Successfully"
			return render(request,'profile.html',{'customer':customer,'msg':msg,'artist':artist})
		else:
			return render(request,'profile.html',{'customer':customer,'artist':artist})
	except:
		artist_get=Artist.objects.get(email=request.session['email'])
		if request.method=="POST":
			artist_get.lname=request.POST['lname']
			artist_get.fname=request.POST['fname']
			artist_get.email=request.POST['email']
			artist_get.mobile=request.POST['mobile']
			artist_get.about=request.POST['about']
			artist_get.facebook=request.POST['facebook']
			artist_get.instagram=request.POST['instagram']
			artist_get.twitter=request.POST['twitter']
			try:
				artist_get.profile_pic=request.FILES['profile_pic']
			except:
				pass
			artist_get.save()
			request.session['profile_pic']=artist_get.profile_pic.url
			msg="Profile Updated Successfully"
			return render(request,'profile.html',{'artist_get':artist_get,'msg':msg,'artist':artist})
		else:
			return render(request,'profile.html',{'artist_get':artist_get,'artist':artist})

def artist_details(request):
	artist=Artist.objects.all().order_by('id')[:3]
	artist_info=Artist.objects.get()
	return render (request,'artist-details.html',{'artist':artist,'artist_info':artist_info})





