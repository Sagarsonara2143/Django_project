from django.contrib import admin
from .models import Product_master,Product_sub_cat

# Register your models here.
admin.site.register(Product_master),
admin.site.register(Product_sub_cat)