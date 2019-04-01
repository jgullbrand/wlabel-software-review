from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()
	company_name = forms.CharField(max_length=100)
	job_title = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ['username', 'email', 'company_name', 'job_title', 'password1', 'password2']
	
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None	