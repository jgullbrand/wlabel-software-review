from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Company

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
	
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None	

class UpdateProfile(forms.ModelForm):
	username = forms.CharField(max_length=100, label='', widget=forms.Textarea(attrs={'cols': 35, 'rows': 1}))
	email = forms.EmailField(required=True, label='', widget=forms.Textarea(attrs={'cols': 35, 'rows': 1}))

	class Meta:
		model = User
		fields = ['username', 'email']
		help_texts = {
            'username': None,
            'email': None,
        }


class UpdateCompany(forms.ModelForm):

	class Meta:
		model = Company
		fields = ['company_name', 'company_logo']  