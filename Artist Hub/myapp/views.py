from django.shortcuts import render,redirect
from .models import Contact,Customer,Artist
# Create your views here.


def index(request):
	artist=Artist.objects.all()
	print(artist)
	return render(request,'index.html',{'artist':artist})

def about(request):
	artist=Artist.objects.all()	
	return render(request,'about-us.html',{'artist':artist})

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
	artist=Artist.objects.all()
	return render(request,'artist.html',{'artist':artist})

def login(request):
	
	if request.method=="POST":
		try:
			artist=Artist.objects.get(email=request.POST['email'])
			if artist.password==request.POST['password']:
				request.session['email']=artist.email
				request.session['fname']=artist.fname
				request.session['profile_pic']=artist.profile_pic.url
				return redirect("index")
			else:
				msg="Password does not matched"
				return render(request,'login.html',{'msg':msg,})
		except:
			try:
				customer=Customer.objects.get(email=request.POST['email'])
				if customer.password==request.POST['password']:
					request.session['email']=customer.email
					request.session['fname']=customer.fname
					request.session['profile_pic']=customer.profile_pic.url
					return redirect("index")
				else:
					msg="Password does not matched"
					return render(request,'login.html',{'msg':msg,})
			except:
				msg="Email does not registered"
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
	if request.method=="POST":
		try:
			Artist.objects.get(mobile=request.POST['mobile'])
			msg="Mobile Number is already registered"
			return render(request,'signup-artist.html',{'msg':msg,})
		except:
			try:
				Artist.objects.get(email=request.POST['email'])
				msg="Email Id is already registered"
				return render(request,'signup-artist.html',{'msg':msg,})
			except:
				if request.POST['password']==request.POST['cpassword']:
					Artist.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						about=request.POST['about'],
						facebook=request.POST['facebook'],
						instagram=request.POST['instagram'],
						twitter=request.POST['twitter'],
						password=request.POST['password'],
						profile_pic=request.FILES['profile_pic']
						)
					msg="Signup Successfully"
					return render(request,'login.html',{'msg':msg,})
				else:
					msg="Password & Confirm password does not match"
					return render(request,'signup-artist.html',{'msg':msg,})
	else:
		return render(request,'signup-artist.html')
	

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






