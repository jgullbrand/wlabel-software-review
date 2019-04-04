from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
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

class CreatePosting(CreateView):
	model = SoftwareProduct
	template_name = 'reviews/product_listing.html'
	fields = ['product_name', 'product_website', 'product_description', 'pricing_details', 
				'free_trial_offered', 'category']	

	def form_valid(self,form):
		form.instance.admin_user = self.request.user
		return super().form_valid(form)


class ProductView(DetailView):	
	model = SoftwareProduct
	template_name = 'reviews/product_detail.html'	