from django.shortcuts import render
from . models import Contact,User

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
					password=request.POST['password']
					)
				msg="User Signup Successfully.."
				return render(request,'signup.html',{'msg':msg})
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
	return render(request,'change-password.html')