from django.shortcuts import render,redirect
from .models import Contact,Customer
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
		return render(request,'contact.html',{'msg':msg,})
	else:
		return render(request,'contact.html')

def artist(request):
	
	return render(request,'artist.html')

def login(request):
	
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				request.session['usertype']=user.usertype
				return redirect("index")
			else:
				msg="Password does not matched"
				return render(request,'login.html',{'msg':msg,})
		except:
			msg="Email not registered"
			return render(request,'login.html',{'msg':msg,})
	else:
		return render(request,'login.html')

def signup(request):
	
	if request.method=="POST":
		try:
			Customer.objects.get(mobile=request.POST['mobile'])
			msg="Mobile Number is already registered"
			return render(request,'signup.html',{'msg':msg,})
		except:
			try:
				Customer.objects.get(email=request.POST['email'])
				msg="Email Id is already registered"
				return render(request,'signup.html',{'msg':msg,})
			except:
				if request.POST['password']==request.POST['cpassword']:
					Customer.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						address=request.POST['address'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
						)
					msg="Signup Successfully"
					return render(request,'login.html',{'msg':msg,})
				else:
					msg="Password & Confirm password does not match"
					return render(request,'signup.html',{'msg':msg,})
	else:
		return render(request,'signup.html')


def signup_artist(request):
	return render (request,'signup-artist.html')



def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		del request.session['usertype']
		return redirect('login')
	except:
		return redirect('login')

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		
		user.usertype=request.POST['usertype']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		
		msg="Profile Updated Successfully"
		return render(request,'profile.html',{'user':user,'msg':msg,})
	else:
		return render(request,'profile.html',{'user':user,})






