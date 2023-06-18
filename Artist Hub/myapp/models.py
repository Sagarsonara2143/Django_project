from django.db import models

# Create your models here.
class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.BigIntegerField()
	message=models.TextField(max_length=500)

	def __str__(self):
		return self.name

class Customer(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.BigIntegerField()
	address=models.TextField(max_length=500)
	password=models.CharField(max_length=50)
	profile_pic=models.ImageField(upload_to='profile_pic')

	def __str__(self):
		return self.fname+" "+ self.lname

class Artist(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.BigIntegerField()	
	about=models.TextField(max_length=500)
	facebook=models.CharField(max_length=100)
	instagram=models.CharField(max_length=100)
	twitter=models.CharField(max_length=100)
	password=models.CharField(max_length=50)
	profile_pic=models.ImageField(upload_to='profile_pic')

	def __str__(self):
		return self.fname+" "+ self.lname