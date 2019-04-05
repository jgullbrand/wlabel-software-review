from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from .models import SoftwareProduct, Reviews, Category


class HomeView(ListView):
	model = Category
	template_name = 'reviews/home.html'
	context_object_name = 'categories'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['product_list'] = SoftwareProduct.objects.all()
		return context	

class CategoryView(ListView):	
	model = SoftwareProduct
	template_name = 'reviews/categories.html'
	context_object_name = 'product_list'	

	def get_queryset(self):
		category = get_object_or_404(Category, category_url=self.kwargs.get('category_url'))
		return SoftwareProduct.objects.filter(category=category)

class CreatePosting(LoginRequiredMixin, CreateView):
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


class UpdatePosting(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = SoftwareProduct
	template_name = 'reviews/product_listing.html'
	fields = ['product_name', 'product_website', 'product_description', 'pricing_details', 
				'free_trial_offered', 'category']

	def get_success_url(self):
		return reverse('profile')	

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.admin_user:
			return True
		return False					

class DeletePosting(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = SoftwareProduct
	template_name = 'reviews/delete_product_listing.html'

	def get_success_url(self):
		return reverse('profile')	

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.admin_user:
			return True
		return False				

class CreateReview(LoginRequiredMixin, CreateView):
	model = Reviews
	template_name = 'reviews/create_review.html'
	fields = ['review_title', 'review_description', 'score']	

	def form_valid(self,form):
		form.instance.user = self.request.user
		form.instance.software_product = SoftwareProduct.objects.get(id=self.kwargs.get('pk'))
		return super().form_valid(form)		

	def get_success_url(self):
		return reverse('product-view', kwargs={'pk': self.kwargs.get('pk')})	


def results(request):
	product_list = SoftwareProduct.objects.all()
	category_list = Category.objects.all()
	query = request.GET.get("q")
	if query:
		product_list = product_list.filter(
			Q(product_name__icontains=query) |
			Q(product_description__icontains=query)
			).distinct()
	context = {'product_list': product_list, 'category_list': category_list}
	return render(request, 'reviews/results.html', context)

