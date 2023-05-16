from django.shortcuts import render,redirect
from .models import User,Product,Wishlist,Cart
import requests
import random
import stripe
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.utils import timezone


stripe.api_key = settings.STRIPE_PRIVATE_KEY
YOUR_DOMAIN = 'http://localhost:8000'

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
	try:
		user=User.objects.get(email=request.session['email'])
		if user.usertype=="seller":
			return redirect('seller-index')
		else:
			products=Product.objects.all()
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			return render(request,'index.html',{'products':products,'carts':carts,'net_price':net_price,'total_qty':total_qty})
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
			try:
				User.objects.get(mobile=request.POST['mobile'])	
				msg="Mobile Number Already Registred"
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
				if user.usertype=="seller":
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					request.session['usertype']=user.usertype
					return redirect("seller-index")	
				else:
					request.session['email']=user.email
					request.session['fname']=user.fname
					request.session['profile_pic']=user.profile_pic.url
					request.session['usertype']=user.usertype
					wishlists=Wishlist.objects.filter(user=user)
					request.session['wishlist_count']=len(wishlists)
					carts=Cart.objects.filter(user=user,paymemt_status=False)
					request.session['cart_count']=len(carts)
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
		del request.session['wishlist_count']
		del request.session['cart_count']
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
				msg="Password changed successfully"
				return redirect('logout') 
			else:
				if user.usertype=="seller":
					msg="New Password & confirm New Password does not matched"
					return render(request,'seller-change-password.html',{'msg':msg})
				else:
					carts=Cart.objects.filter(user=user,paymemt_status=False)
					net_price=0
					total_qty=0
					for i in carts:
						net_price=net_price+i.total_price
						total_qty=total_qty+i.product_qty
					msg="New Password & confirm New Password does not matched"
					return render(request,'change-password.html',{'carts':carts,'msg':msg,'net_price':net_price,'total_qty':total_qty})	
		else:
			if user.usertype=="seller":
				msg="Incorrect Old Password"
				return render(request,'seller-change-password.html',{'msg':msg})
			else:
				carts=Cart.objects.filter(user=user,paymemt_status=False)
				net_price=0
				total_qty=0
				for i in carts:
					net_price=net_price+i.total_price
					total_qty=total_qty+i.product_qty
				msg="Incorrect Old Password"
				return render(request,'change-password.html',{'msg':msg,'carts':carts,'net_price':net_price,'total_qty':total_qty})
	else:
		if user.usertype=="seller":
			return render(request,'seller-change-password.html')
		else:
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			return render(request,'change-password.html',{'carts':carts,'net_price':net_price,'total_qty':total_qty})

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
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			msg="Profile Updated Successfully"
			return render(request,'profile.html',{'user':user,'msg':msg,'carts':carts,'net_price':net_price,'total_qty':total_qty})
	else:
		if user.usertype=="seller":
			return render(request,'seller-profile.html',{'user':user})
		else:
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			return render(request,'profile.html',{'user':user,'carts':carts,'net_price':net_price,'total_qty':total_qty})


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
	try:
		user=User.objects.get(user=user)
		if request.session.email():
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			products=Product.objects.filter(product_cat="Laptop")
			return render (request,"index.html",{'carts':carts,'net_price':net_price,'total_qty':total_qty,'products':products})
		else:
			products=Product.objects.filter(product_cat="Laptop")
			return render (request,"index.html",{'products':products})
	except:
		products=Product.objects.filter(product_cat="Laptop")
		return render (request,"index.html",{'products':products})


def cameras(request):
	try:
		user=User.objects.get(user=user)
		if request.session.email():
			products=Product.objects.filter(product_cat="Camera")
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			return render (request,"index.html",{'products':products,'carts':carts,'net_price':net_price,'total_qty':total_qty})
		else:
			products=Product.objects.filter(product_cat="Camera")
			return render (request,"index.html",{'products':products})
	except:
		products=Product.objects.filter(product_cat="Camera")
		return render (request,"index.html",{'products':products})

def accessories(request):
	try:
		user=User.objects.get(user=user)
		if request.session.email():
			products=Product.objects.filter(product_cat="Accessories")
			carts=Cart.objects.filter(user=user,paymemt_status=False)
			net_price=0
			total_qty=0
			for i in carts:
				net_price=net_price+i.total_price
				total_qty=total_qty+i.product_qty
			return render (request,"index.html",{'products':products,'carts':carts,'net_price':net_price,'total_qty':total_qty})
		else:
			products=Product.objects.filter(product_cat="Accessories")
			return render (request,"index.html",{'products':products})
	except:
		products=Product.objects.filter(product_cat="Accessories")
		return render (request,"index.html",{'products':products})

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


def product_details(request,pk):
	user=User.objects.get(email=request.session['email'])
	#carts=Cart.objects.get(user=user)
	wishlist_flag=False
	cart_flag=False
	product=Product.objects.get(pk=pk)
	try:
		Wishlist.objects.get(user=user,product=product)
		wishlist_flag=True
	except:
		pass

	try:
		Cart.objects.get(user=user,product=product,paymemt_status=False)
		cart_flag=True
	except:
		pass
	carts=Cart.objects.filter(user=user,paymemt_status=False)
	net_price=0
	total_qty=0
	for i in carts:
		net_price=net_price+i.total_price
		total_qty=total_qty+i.product_qty
	return render (request,"product-details.html",{'products':products,'wishlist_flag':wishlist_flag,'cart_flag':cart_flag,'carts':carts,'net_price':net_price,'total_qty':total_qty})

def wishlist(request):
	user=User.objects.get(email=request.session['email'])
	wishlists=Wishlist.objects.filter(user=user)
	request.session['wishlist_count']=len(wishlists)
	carts=Cart.objects.filter(user=user,paymemt_status=False)
	net_price=0
	total_qty=0
	for i in carts:
		net_price=net_price+i.total_price
		total_qty=total_qty+i.product_qty
	return render(request,'wishlist.html',{'wishlists':wishlists,'carts':carts,'net_price':net_price,'total_qty':total_qty})


def add_to_wishlist(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Wishlist.objects.create(
		product=product,
		user=user
		)
	return redirect('wishlist')

def remove_from_wishlist(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	wishlist=Wishlist.objects.get(user=user,product=product)
	wishlist.delete()
	return redirect('wishlist')
	
def cart(request):
	net_price=0
	total_qty=0
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,paymemt_status=False)
	request.session['cart_count']=len(carts)
	for i in carts:
		net_price=net_price+i.total_price
		total_qty=total_qty+i.product_qty
	return render(request,'cart.html',{'carts':carts,'net_price':net_price,'total_qty':total_qty})


def add_to_cart(request,pk):
	product=Product.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])
	Cart.objects.create(
		product=product,
		user=user,
		product_price=product.product_price,
		product_qty=1,
		total_price=product.product_price,
		paymemt_status=False
		)
	product.cart_status=True
	product.save()
	return redirect('cart')

def remove_from_cart(request,pk):
	user=User.objects.get(email=request.session['email'])
	product=Product.objects.get(pk=pk)
	cart=Cart.objects.get(user=user,product=product)
	cart.delete()
	product.cart_status=False
	product.save()
	return redirect('cart')

def change_cart_qty(request):
	cart_id=int(request.POST['cart_id'])
	product_qty=int(request.POST['product_qty'])
	cart=Cart.objects.get(pk=cart_id)
	cart.product_qty=product_qty
	cart.total_price=product_qty*cart.product_price
	cart.save()
	return redirect('cart')	

def checkout(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,paymemt_status=False)
	net_price=0
	for i in carts:
		net_price=net_price+i.total_price
	return render(request,'checkout.html',{'user':user,'carts':carts,'net_price':net_price})


@csrf_exempt
def create_checkout_session(request):
 #Updated- creating Order object

 amount=int(json.load(request)['post_data'])
 final_amount=amount * 100

 session=stripe.checkout.Session.create(
	payment_method_types=['card'],
	line_items=[{
	'price_data': {
	'currency': 'inr',
	'product_data': {
	'name': 'Intro to Django Course',
	},
	'unit_amount':final_amount,
	},
	'quantity': 1,
	}],
	mode='payment',
	success_url=YOUR_DOMAIN + '/success.html',
	cancel_url=YOUR_DOMAIN + '/cancel.html',
	)
 return JsonResponse({'id':session.id})

def success(request):
	user=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(user=user,paymemt_status=False)

	for i in carts:
		i.paymemt_status=True
		i.ordered_date=timezone.now()
		i.save()
		product=Product.objects.get(id=i.product.id)
		product.cart_status=False
		product.save()

	carts=Cart.objects.filter(user=user,paymemt_status=False)
	request.session['cart_count']=len(carts)
	return render(request,'success.html',{'carts':carts})

def cancel(request):
	return render(request,'cancel.html')


def myorder(request):
	user=User.objects.get(email=request.session['email'])
	purchased_carts=Cart.objects.filter(user=user,paymemt_status=True)
	carts=Cart.objects.filter(user=user,paymemt_status=False)
	net_price=0
	total_qty=0
	for i in carts:
		net_price=net_price+i.total_price
		total_qty=total_qty+i.product_qty
	return render(request,'myorder.html',{'purchased_carts':purchased_carts,'carts':carts,'net_price':net_price,'total_qty':total_qty})

def seller_order(request):
	seller=User.objects.get(email=request.session['email'])
	carts=Cart.objects.filter(paymemt_status=True)
	orders = []
	for i in carts:
		if i.product.seller==seller:
			orders.append(i)
	print(orders)
	return render(request,'seller-order.html',{'orders':orders})



