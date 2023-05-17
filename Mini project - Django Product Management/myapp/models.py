from django.db import models

# Create your models here.

class Product_mst(models.Model):
	product_name=models.CharField(max_length=50)

	def __str__(self):
		return self.product_name


class Product_sub_cat(models.Model):
	product=models.ForeignKey(Product_mst,on_delete=models.CASCADE)
	price=models.CharField(max_length=100)
	image=models.ImageField(upload_to="product_image")
	model=models.CharField(max_length=100)
	RAM=models.PositiveSmallIntegerField()

	def __str__(self):
		return self.Product_mst.product_name+" "+self.model
