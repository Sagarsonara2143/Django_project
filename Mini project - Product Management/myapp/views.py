from django.shortcuts import render
from .models import Product_master,Product_sub_cat
from django.db.models import Q

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


def edit(request,pk):
	sub_product=Product_sub_cat.objects.get(pk=pk)
	#print(sub_product)
	return render(request,"edit.html",{'sub_product':sub_product})
	
def update(request,pk):
	sub_product=Product_sub_cat.objects.get(pk=pk)
	sub_product.price=request.POST['price']
	sub_product.model=request.POST['model']
	sub_product.RAM=request.POST['ram']

	sub_product.save()
	msg="Product Updated Successfully"
	product=Product_master.objects.all()
	sub_product=Product_sub_cat.objects.all()
	return render(request,"product.html",{'msg':msg,'product':product,'sub_product':sub_product})
	

def delete(request,pk):	
	sub_product=Product_sub_cat.objects.get(pk=pk)
	sub_product.delete()
	msg="Product Deleted Successfully"
	product=Product_master.objects.all()
	sub_product=Product_sub_cat.objects.all()
	return render(request,"product.html",{'msg':msg,'product':product,'sub_product':sub_product})
	

def product_manager(request):
	sub_product=Product_sub_cat.objects.all()
	return render(request,'view-product.html',{'sub_product':sub_product})


def search(request):
	if 'q' in request.GET:
		q=request.GET['q']
		multiple_q=Q(Q(price__icontains=q) | Q(model__icontains=q) | Q(RAM__icontains=q) )
		sub_product=Product_sub_cat.objects.filter(multiple_q)
		return render (request,'view-product.html',{'sub_product':sub_product})
	else:
		msg="Not Found ..!!"
		return render (request,'view-product.html',{'msg':msg})











