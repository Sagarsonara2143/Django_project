from django.shortcuts import render
from .models import Contact
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
	return render(request,'index.html')

def about(request):
	return render(request,'about-us.html')

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
	return render(request,'artist.html')

def login(request):
	return render(request,'login.html')

def signup(request):
	return render(request,'signup-option.html')