from django.shortcuts import render

#will plan to change these to generic class based views

def home(request):
	context = {} # will update later
	return render(request, 'reviews/base.html', context)

def categories(request):
	context = {} # will update later
	return render(request, 'reviews/categories.html', context)

def profile(request):
	context = {} # will update later
	return render(request, 'reviews/profile.html', context)	