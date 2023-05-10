from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()
	address=models.TextField(max_length=100)
	city=models.CharField(max_length=100)
	zipcode=models.PositiveSmallIntegerField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to='profile_pic',default="")
	usertype=models.CharField(max_length=100,default="buyer")
	
	def __str__(self):
		return self.fname+" "+self.lname+" - "+self.usertype


class Product(models.Model):
	category=(
		('Laptop','Laptop'),
		('Accessories','Accessories'),
		('Camera','Camera'),
		)
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_cat=models.CharField(max_length=100, choices=category)
	product_name=models.CharField(max_length=100)
	product_desc=models.TextField()
	product_price=models.PositiveSmallIntegerField()
	product_image=models.ImageField(upload_to='product_image/')
	product_stock=models.PositiveSmallIntegerField()
	cart_status=models.BooleanField(default=False)

	def __str__(self):
		return self.seller.fname+" - "+self.product_name


class Wishlist(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.user.fname + " - "+self.product.product_name	


class Cart(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)
	product_price=models.PositiveSmallIntegerField()
	product_qty=models.PositiveSmallIntegerField()
	total_price=models.PositiveSmallIntegerField()
	paymemt_status=models.BooleanField(default=False)



	def __str__(self):
		return self.user.fname + " - "+self.product.product_name	


