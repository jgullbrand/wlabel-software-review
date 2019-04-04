from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	company_name = models.CharField(max_length=100, blank=True, null = True)
	company_logo = models.ImageField(default='default.jpg', upload_to='company_pics')

	def __str__(self):
		return f'{self.user.username}: {self.company_name}'