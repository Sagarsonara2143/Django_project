from django.shortcuts import render
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