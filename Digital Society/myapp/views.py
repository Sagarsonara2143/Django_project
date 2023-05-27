from django.shortcuts import render

from .models import User

# Create your views here.
def login(request):
	return render(request,'login.html')

def signup(request):
	if request.method=="POST":
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
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						gender=request.POST['gender'],
						address=request.POST['address'],
						password=request.POST['password']
						)
					msg="User Registration successfully"
					return render(request,'login.html',{'msg':msg})
				else:
					msg="Password and confirm password does not matched"
					return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')