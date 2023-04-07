from django.shortcuts import render
from . models import Contact

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
	if request.method="POST":
		User.objects.create(
			fname=request.POST['fname'],
			lname=request.POST['lname'],
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			gender=request.POST['gender'],
			address=request.POST['address'],
			password=request.POST['password']
			)
		
	else:
		return render(request,'signup.html')

def login(request):
	return render(request,'login.html')
