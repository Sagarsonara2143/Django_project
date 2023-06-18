from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.BigIntegerField()
	message=models.TextField(max_length=500)

	def __str__(self):
		return self.name

class User(models.Model):
	category=(
		('Artist','Artist'),
		('Customer','Customer'),
		)
	usertype=models.CharField(max_length=100, choices=category)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.BigIntegerField()
	address=models.TextField(max_length=500)
	password=models.CharField(max_length=50)
	profile_pic=models.ImageField(upload_to='profile_pic')

	def __str__(self):
		return self.fname+" "+ self.lname + " - "+ self.usertype