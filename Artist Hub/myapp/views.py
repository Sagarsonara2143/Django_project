from django.shortcuts import render
from .models import Contact,User
# Create your views here.

def validate_email(request):
	email=request.GET.get('email')
	data={
		'is_taken':User.objects.filter(email__iexact=email).exists()
	}		
	return JsonResponse(data)

def validate_mobile(request):
	mobile=request.GET.get('mobile')
	data={
		'is_taken':User.objects.filter(mobile__iexact=mobile).exists()
	}		
	return JsonResponse(data)

def validate_pwd(request):
	pwd=request.GET.get('pwd')
	cpwd=request.GET.get('cpwd')
	data={
		'is_taken': pwd != cpwd
	}		
	return JsonResponse(data)


def index(request):
	user=User.objects.all()
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	print(artists)
	return render(request,'index.html',{'artists':artists})

def about(request):
	user=User.objects.all()
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	print(artists)
	return render(request,'about-us.html',{'artists':artists})

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			message=request.POST['message']
			)
		msg="Message Sent Successfully"
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')

def artist(request):
	user=User.objects.all()
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	print(artists)
	return render(request,'artist.html',{'artists':artists})

def login(request):
	return render(request,'login.html')

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(mobile=request.POST['mobile'])
			msg="Mobile Number is already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			try:
				User.objects.get(email=request.POST['email'])
				msg="Email Id is already registered"
				return render(request,'signup.html',{'msg':msg})
			except:
				if request.POST['password']==request.POST['cpassword']:
					User.objects.create(
						usertype=request.POST['usertype'],
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
						)
					msg="Signup Successfully"
					return render(request,'login.html',{'msg':msg})
				else:
					msg="Password & Confirm password does not match"
					return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')