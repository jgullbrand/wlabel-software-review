from django.shortcuts import render, redirect
from .forms import RegistrationForm, UpdateProfile
from django.contrib.auth import authenticate, login

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



def profile(request):
	if request.method == 'POST':
		form = UpdateProfile(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UpdateProfile(instance=request.user)	


	context = {'form': form}
	return render(request, 'users/profile.html', context)
