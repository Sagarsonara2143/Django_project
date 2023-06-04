from django.db import models

# Create your models here.
class User(models.Model):
	usertype=models.CharField(max_length=100, default="member")
	house=models.CharField(max_length=100)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic")

	def __str__(self):
		return self.fname+" "+self.lname