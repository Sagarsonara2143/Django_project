from django.shortcuts import render,redirect
from .models import User,Product
import requests
import random

# Create your views here.

def index(request):
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="seller":
			return redirect('seller-index')
		else:
			products=Product.objects.all()
			return render(request,'index.html',{'products':products})
	except:
		products=Product.objects.all()
		return render(request,'index.html',{'products':products})


def seller_index(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,'seller-index.html',{'products':products})

def signup(request):
	if request.method=="POST":
		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Id is already registered"
			return render(request,'signup.html',{'msg':msg})
		except:
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					email=request.POST['email'],
					mobile=request.POST['mobile'],
					address=request.POST['address'],
					city=request.POST['city'],
					zipcode=request.POST['zipcode'],
					password=request.POST['password'],
					profile_pic=request.FILES['profile_pic'],
					usertype=request.POST['usertype']
					)
				msg="User Sign Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm password does not matched"
				return render(request,'signup.html',{'msg':msg})
	else:
		return render(request,'signup.html')


def login(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['profile_pic']=user.profile_pic.url
				request.session['usertype']=user.usertype

				if user.usertype=="seller":
					return redirect("seller-index")	
				else:
					return redirect('index')
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
		return render(request,'login.html')
	except:
		return render(request,'login.html')	

def change_password(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		if user.password==request.POST['old_password']:
			if request.POST['new_password']==request.POST['cnew_password']:
				user.password=request.POST['new_password']
				user.save()
				return redirect ('logout') 
			else:
				if user.usertype=="seller":
					msg="New Password & confirm New Password does not matched"
					return render(request,'seller-change-password.html',{'msg':msg})
				else:
					msg="New Password & confirm New Password does not matched"
					return render(request,'change-password.html',{'msg':msg})	
		else:
			if user.usertype=="seller":
				msg="Incorrect Old Password"
				return render(request,'seller-change-password.html',{'msg':msg})
			else:
				msg="Incorrect Old Password"
				return render(request,'change-password.html',{'msg':msg})
	else:
		if user.usertype=="seller":
			return render(request,'seller-change-password.html')
		else:
			return render(request,'change-password.html')

def forgot_password(request):
	if request.method=="POST":
		try:
			user=User.objects.get(mobile=request.POST['mobile'])
			otp = random.randint(1000,9999)
			mobile=user.mobile
			url = "https://www.fast2sms.com/dev/bulkV2"
			querystring = {"authorization":"EWmfIayCLFdvOxl1MJZkQDiVYjbB740z8oSAwc6NGepUugq9hKQkrUqs5fK2o3Fza0WheDdSG91JcTYM","variables_values":str(otp),"route":"otp","numbers":str(mobile)}
			headers = {'cache-control': "no-cache"}
			response = requests.request("GET", url, headers=headers, params=querystring)
			print(response.text)
			msg="OTP Sent Successfully"
			return render(request,"verify-otp.html",{'msg':msg,'otp':otp,'mobile':mobile})
		except:
			msg="Mobile Number not registered"
			return render(request,"forgot-password.html",{'msg':msg})
	else:
		return render(request,"forgot-password.html")

def verify_otp(request):
	otp=request.POST['otp']
	mobile=request.POST['mobile']
	uotp=request.POST['uotp']

	if otp==uotp:
		return render(request,"new-password.html",{'mobile':mobile})	
	else:
		msg="Invalid OTP Entered"
		return render(request,"verify-otp.html",{'msg':msg,'mobile':mobile,'otp':otp})

def new_password(request):
	
	n_pwd=request.POST['new_password']
	cn_pwd=request.POST['cnew_password']
	if n_pwd==cn_pwd:
		user=User.objects.get(mobile=request.POST['mobile'])
		user.password=n_pwd
		user.save()
		return redirect('login')
	else:
		msg="New Password & Confirm New Password does not Matched"
		return render(request,"new-password.html",{'msg':msg})

def profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.address=request.POST['address']
		user.city=request.POST['city']
		user.zipcode=request.POST['zipcode']
		try:
			user.profile_pic=request.FILES['profile_pic']
		except:
			pass
		user.save()
		request.session['profile_pic']=user.profile_pic.url
		if user.usertype=="seller":
			msg="Profile Updated Successfully"
			return render(request,'seller-profile.html',{'user':user,'msg':msg})
		else:
			msg="Profile Updated Successfully"
			return render(request,'profile.html',{'user':user,'msg':msg})
	else:
		if user.usertype=="seller":
			return render(request,'seller-profile.html',{'user':user})
		else:
			return render(request,'profile.html',{'user':user})


def seller_add_product(request):
	seller=User.objects.get(email=request.session['email'])
	if request.method=="POST": 
		Product.objects.create(
			seller=seller,
			product_cat=request.POST['product_cat'],
			product_name=request.POST['product_name'],
			product_desc=request.POST['product_desc'],
			product_price=request.POST['product_price'],
			product_stock=request.POST['product_stock'],
			product_image=request.FILES['product_image']
			)
		msg="Product Added Successfully"
		return render(request,"seller-add-product.html",{'msg':msg})
	else:
		return render(request,"seller-add-product.html")

def seller_view_product(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller)
	return render(request,"seller-view-product.html",{'products':products})

def seller_product_details(request,pk):
	product=Product.objects.get(pk=pk)
	return render(request,"seller-product-details.html",{'product':product})

def seller_edit_product(request,pk):
	product=Product.objects.get(pk=pk)
	if request.method=="POST":
		product.product_cat=request.POST['product_cat']
		product.product_name=request.POST['product_name']
		product.product_desc=request.POST['product_desc']
		product.product_price=request.POST['product_price']
		product.product_stock=request.POST['product_stock']
		try:
			product.image=request.FILES['product_image.url']
		except:
			pass

		product.save()
		msg="Product Updated Successfully"
		return render(request,"seller-product-details.html",{'product':product,'msg':msg})

	else:
		return render(request,"seller-edit-product.html",{'product':product})


def seller_product_delete(request,pk):
	product=Product.objects.get(pk=pk)
	product.delete()
	return redirect('seller-view-product')


def laptops(request):
	products=Product.objects.filter(product_cat="Laptop")
	return render (request,"index.html",{'products':products})

def cameras(request):
	products=Product.objects.filter(product_cat="Camera")
	return render(request,"index.html",{'products':products})

def accessories(request):
	products=Product.objects.filter(product_cat="Accessories")
	return render(request,"index.html",{'products':products})

def seller_laptops(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller,product_cat="Laptop")
	return render(request,"seller-index.html",{'products':products,'seller':seller})	

def seller_accessories(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller,product_cat="Accessories")
	return render(request,"seller-index.html",{'products':products,'seller':seller})

def seller_cameras(request):
	seller=User.objects.get(email=request.session['email'])
	products=Product.objects.filter(seller=seller,product_cat="Camera")
	return render(request,"seller-index.html",{'products':products,'seller':seller})











