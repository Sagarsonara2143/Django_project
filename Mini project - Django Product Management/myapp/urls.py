from django.urls import path
from . import views
from .models import Product_master,Product_sub_cat

urlpatterns = [
    path('',views.index, name='index'),
    path('product-master',views.product_master,name="product-master"),
    path('product-add',views.product_add,name="product-add"),
]
