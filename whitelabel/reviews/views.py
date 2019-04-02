from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import SoftwareProduct, Reviews, Category
from django.contrib.auth.models import User

class HomeView(ListView):
	model = Category
	template_name = 'reviews/home.html'
	context_object_name = 'categories'


class CategoryView(ListView):	
	model = SoftwareProduct
	template_name = 'reviews/categories.html'
	context_object_name = 'product_list'	

	def get_queryset(self):
		category = get_object_or_404(Category, category_url=self.kwargs.get('category_url'))
		return SoftwareProduct.objects.filter(category=category)


class CreateProduct(CreateView):
	