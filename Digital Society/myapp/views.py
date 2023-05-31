from django.shortcuts import render, redirect

from .models import User

# Create your views here.


def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(house=request.POST['house'])
			msg="House Number already registered"
			return render(request,"signup.html",{'msg':msg})
		except:
			try:
				user=User.objects.get(email=request.POST['email'])
				msg="Email ID already registered"
				return render(request,"signup.html",{'msg':msg})
			except:
				try:
					user=User.objects.get(mobile=request.POST['mobile'])
					msg="Mobile Number is already registered"
					return render(request,"signup.html",{'msg':msg})
				except:
					if request.POST['password']==request.POST['cpassword']:
						User.objects.create(
							usertype=request.POST['usertype'],
							house=request.POST['house'],
							fname=request.POST['fname'],
							lname=request.POST['lname'],
							email=request.POST['email'],
							mobile=request.POST['mobile'],	
							password=request.POST['password']
							)
						msg="User Registration successfully"
						return render(request,'login.html',{'msg':msg})
					else:
						msg="Password and confirm password does not matched"
						return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')


def index(request):
	return render(request,'index.html')


def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="member":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['usertype']=user.usertype
					return redirect('index')	
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['usertype']=user.usertype
					return redirect('index')
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')

	