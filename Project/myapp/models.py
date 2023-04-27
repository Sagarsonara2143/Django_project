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