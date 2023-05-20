from django.shortcuts import render
from .models import Product_master,Product_sub_cat

# Create your views here.

def index(request):
	return render(request,'index.html')

def product_master(request):
	return render(request,'product-master.html')

def product_master_add(request):
	if request.method=="POST":
		Product_master.objects.create(
			product_name=request.POST['product_name']
			)
		
		msg="Product Added Successfully"
		return render(request,'product-master.html',{'msg':msg})
	else:
		
		return render(request,"product-master.html")

def sub_product_add(request):
	if request.method=="POST":
		name=Product_master.objects.get(product_name=request.POST['name'])
		Product_sub_cat.objects.create(
			product=name,
			price=request.POST['price'],
			model=request.POST['model'],
			RAM=request.POST['ram']
			)
		msg="Product Added Successfully"
		product=Product_master.objects.all()
		sub_product=Product_sub_cat.objects.all()
		return render(request,"product.html",{'product':product,'sub_product':sub_product})
	else:
		product=Product_master.objects.all()
		sub_product=Product_sub_cat.objects.all()
		print(sub_product)
		return render(request,"product.html",{'product':product,'sub_product':sub_product})

