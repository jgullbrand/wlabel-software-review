from django.shortcuts import render

def home(request):
	context = {} # will update later
	return render(request, 'reviews/home.html', context)
