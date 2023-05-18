from django.shortcuts import render
from .models import Product_master,Product_sub_cat

# Create your views here.

def index(request):
	return render(request,'index.html')

def product_master(request):
	return render(request,'product-master.html')

def product_add(request):
	if request.method=="POST":
		Product_master.objects.create(
			product_name=request.POST['product_name']
			)	
		msg="Product Added Successfully"
		product=Product_master.objects.all()
		#print(product)
		return render(request,'product-master.html',{'msg':msg,'product':product})
	else:
		product=Product_master.objects.all()
		return render(request,"product-master.html",{'product':product})