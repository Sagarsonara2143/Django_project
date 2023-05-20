from django.urls import path
from . import views
from .models import Product_master,Product_sub_cat

urlpatterns = [
    path('',views.index, name='index'),
    path('product-master/',views.product_master,name="product-master"),
    path('product-master-add/',views.product_master_add,name="product-master-add"),
    path('sub-product-add/',views.sub_product_add,name='sub-product-add'),
    path('edit/<int:pk>/',views.edit,name='edit'),
    path('update/<int:pk>',views.update,name='update'),
    path('delete/<int:pk>',views.delete,name='delete'),
]
