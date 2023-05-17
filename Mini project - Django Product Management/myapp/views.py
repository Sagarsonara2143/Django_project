from django.shortcuts import render
from .models import Product_master,Product_sub_cat

# Create your views here.

def index(request):
	return render(request,'index.html')

def product_master(request):
	return render(request,'product-master.html')