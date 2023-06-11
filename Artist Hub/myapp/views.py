from django.shortcuts import render
from .models import Contact
# Create your views here.

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