from django.shortcuts import render, redirect

from .models import User

# Create your views here.


def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(house=request.POST['house'])
			msg="House Number already registered"
			return render(request,"signup.html",{'msg':msg})
		except:
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
							usertype=request.POST['usertype'],
							house=request.POST['house'],
							fname=request.POST['fname'],
							lname=request.POST['lname'],
							email=request.POST['email'],
							mobile=request.POST['mobile'],	
							password=request.POST['password'],
							profile_pic=request.FILES['profile_pic']
							)
						msg="User Registration successfully"
						return render(request,'login.html',{'msg':msg})
					else:
						msg="Password and confirm password does not matched"
						return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')


def index(request):
	user=User.objects.get(email=request.session['email'])
	
	try:	
		if user.usertype=="member":
			return redirect('member-index')
		elif user.usertype=="chairman":
			return redirect('chairman-index')
		else:
			return redirect('watchman-index')
	except:
		user=User.objects.get(email=request.session['email'])
		return render(request,'signup.html')

def member_index(request):
	return render(request,"member-index.html")

def chairman_index(request):
	return render(request,"chairman-index.html")

def watchman_index(request):
	return render(request,"watchman-index.html")


def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				if user.usertype=="member":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['usertype']=user.usertype
					request.session['profile_pic']=user.profile_pic.url
					return redirect("member-index")	
				elif user.usertype=="chairman":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['usertype']=user.usertype
					request.session['profile_pic']=user.profile_pic.url
					return redirect("chairman-index")
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['usertype']=user.usertype
					request.session['profile_pic']=user.profile_pic.url
					return redirect("watchman-index")
			else:
				msg="Incorrect Password"
				return render(request,'login.html',{'msg':msg})
		except:
			msg="Email not registered"
			return render(request,'login.html',{'msg':msg})
	else:
		return render(request,'login.html')


def logout(request):
	try:	
		del request.session['email']
		del request.session['fname']
		del request.session['usertype']
		del request.session['profile_pic']
		return render(request,'login.html')
	except:
		return render(request,'login.html')


def member(request):
	user=User.objects.all()
	data=[]
	for i in user:
		if i.usertype=="member":
			data.append(i)
	return render(request, 'member.html',{'user':user,'data':data})
	
def watchman(request):
	user=User.objects.all()
	data=[]
	for i in user:
		if i.usertype=="watchman":
			data.append(i)
	return render(request, 'watchman.html',{'user':user,'data':data})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.usertype=request.POST['usertype']
		user.house=request.POST['house']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		msg="Profile Updated successfully"
		return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		return render(request,'profile.html',{'user':user})