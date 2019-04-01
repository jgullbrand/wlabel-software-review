from django.db import models
from django.contrib.auth.models import User

class SoftwareProduct(models.Model):
	product_name = models.CharField(max_length=150)
	website_link = models.URLField()
	image_logo = models.ImageField()
	description = models.TextField()
	pricing_details = models.CharField(max_length=200)
	free_trial = models.CharField(max_length=3, choices =(('Yes', 'Yes'), ('No', 'No'),))
	admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
	reviews = models.ManyToManyField('Reviews')
	category = models.ManyToManyField('Category')

class Reviews(models.Model):
	score = models.PositiveSmallIntegerField(choices = [(i,i) for i in range(11)])
	review_title = models.CharField(max_length=150)
	review_description = models.TextField()


class Category(models.Model):
	name = models.CharField(max_length=150)


