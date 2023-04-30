from django.db import models

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

	def __str__(self):
		return self.seller.fname+" - "+self.product_name


