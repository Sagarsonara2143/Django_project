from django.shortcuts import render,redirect
from .models import User
import requests
import random

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
					profile_pic=request.FILES['profile_pic']
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
				request.session['profile_pic']=user.profile_pic.url
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
		user=User.objects.get(email=request.session['email'])
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect ('logout') 
			else:
				msg="New Password & confirm New Password does not matched"
				return render(request,'change-password.html',{'msg':msg})	
		else:
			msg="Incorrect Old Password"
			return render(request,'change-password.html',{'msg':msg})
	else:
		return render(request,'change-password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			otp = random.randint(1000,9999)
			mobile=user.mobile
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"EWmfIayCLFdvOxl1MJZkQDiVYjbB740z8oSAwc6NGepUugq9hKQkrUqs5fK2o3Fza0WheDdSG91JcTYM","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)

		except:
			msg="Mobile Number not registered"
			return render(request,"forgot-password.html",{'msg':msg})
	else:
		return render(request,"forgot-password.html")