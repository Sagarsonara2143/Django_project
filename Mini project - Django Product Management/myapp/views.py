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
		return render(request,'product-master.html',{'msg':msg})
	else:
		product=Product_sub_cat.objects.all()
		return render(request,"product-master.html")