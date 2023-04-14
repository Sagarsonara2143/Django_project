from django.db import models

# Create your models here.

class Staff(models.Model):
	category = (
		('trainer','trainer'),
		('counsellor','counsellor'),
		('backoffice','backoffice'),
		('admin','admin')
		)

	staff_cat=models.CharField(max_length=100,choices=category)
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveSmallIntegerField()

	def __str__(self):
		return self.fname+" - "+self.staff_cat
