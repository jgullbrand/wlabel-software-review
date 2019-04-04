from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class SoftwareProduct(models.Model):
	product_name = models.CharField(max_length=150)
	product_website = models.URLField(blank=True, null=True)
	product_description = models.TextField()
	pricing_details = models.TextField()
	free_trial_offered = models.CharField(max_length=3, choices =(('Yes', 'Yes'), ('No', 'No'),))
	admin_user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ManyToManyField('Category')

	def __str__(self):
		return self.product_name

class Reviews(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	software_product = models.ForeignKey(SoftwareProduct, on_delete=models.CASCADE)
	score = models.PositiveSmallIntegerField(choices = [(i,i) for i in range(11)])
	review_title = models.CharField(max_length=150)
	review_description = models.TextField()

	class Meta:
		verbose_name_plural = "Reviews"	

	def __str__(self):
		return f'{self.software_product} : {self.score}'	


class Category(models.Model):
	category_name = models.CharField(max_length=150)
	category_url = models.SlugField(max_length=500, blank=True)

	def save(self, *args, **kwargs):
		self.category_url= slugify(self.category_name)
		super(Category, self).save(*args, **kwargs)    

	class Meta:
		verbose_name_plural = "Categories"		

	def __str__(self):
		return self.category_name


