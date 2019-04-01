from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SoftwareProduct, Reviews, Category

class HomeView(ListView):
	model = Category
	template_name = 'reviews/home.html'
	context_object_name = 'categories'


class CategoriesView(ListView):	
	model = Category
	template_name = 'reviews/categories.html'
	context_object_name = 'categories'	

def software_products(request):
	context = {} # will update later
	return render(request, 'reviews/software_products.html', context)	