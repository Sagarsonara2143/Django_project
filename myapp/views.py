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
		msg="Contact Saved Successfully ,,!"
		return render(request,'contact.html',{'msg':msg})
	else:
		return render(request,'contact.html')

def signup(request):
	return render(request,'signup.html')

def login(request):
	return render(request,'login.html')
