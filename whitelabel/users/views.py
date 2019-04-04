from django.shortcuts import render, redirect
from .forms import RegistrationForm, UpdateProfile, UpdateCompany
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username = request.POST['username']
			password = request.POST['password1']
			user = authenticate(request, username=username, password=password)
			login(request,user)
			return redirect('home')
	else:
		form = RegistrationForm()	


	context = {'form': form}
	return render(request, 'users/register.html', context)


@login_required
def profile(request):
	if "profile_submit" in request.POST and request.method == 'POST':
		profile_form = UpdateProfile(request.POST, instance=request.user)
		if profile_form.is_valid():
			profile_form.save()
			return redirect('profile')	

	elif "company_submit" in request.POST and request.method == 'POST':	
		company_form = UpdateCompany(request.POST, request.FILES, instance=request.user.company)
		if company_form.is_valid():
			company_form.save()
			return redirect('profile')

	else:
		profile_form = UpdateProfile(instance=request.user)	
		company_form = UpdateCompany(instance=request.user.company)

	context = {'profile_form': profile_form, 'company_form': company_form}
	return render(request, 'users/profile.html', context)
