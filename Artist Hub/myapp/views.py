from django.shortcuts import render,redirect
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
	user=User.objects.all().order_by('-id')[:10]
	print(user)
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	print(artists)
	user=User.objects.all()
	drop_artists=artists[:3]
	return render(request,'index.html',{'artists':artists,'drop_artists':drop_artists})

def about(request):
	user=User.objects.all()
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	print(artists)
	drop_artists=artists[:3]
	return render(request,'about-us.html',{'artists':artists,'drop_artists':drop_artists})

def contact(request):
	user=User.objects.all()
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	print(artists)
	drop_artists=artists[:3]

	if request.method=="POST":
		Contact.objects.create(
			name=request.POST['name'],		
			email=request.POST['email'],
			mobile=request.POST['mobile'],
			message=request.POST['message']
			)
		msg="Message Sent Successfully"
		return render(request,'contact.html',{'msg':msg,'drop_artists':drop_artists})
	else:
		return render(request,'contact.html',{'drop_artists':drop_artists})

def artist(request):
	user=User.objects.all()
	#print(user)
	artists=[]
	for i in user:
		if i.usertype=="Artist":
			artists.append(i)
	#print(artists)
	drop_artists=artists[:3]
	return render(request,'artist.html',{'artists':artists,'drop_artists':drop_artists})

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
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not registered"
			return render(request,'login.html',{'msg':msg})
	else:
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


def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['profile_pic']
		del request.session['usertype']
		return render(request,'login.html')
	except:
		return render(request,'login.html')	