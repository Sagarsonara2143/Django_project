from django.db import models

# Create your models here.
class User(models.Model):
	usertype=models.CharField(max_length=50, default="member")
	house=models.CharField(max_length=50)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.fname+" "+self.lname