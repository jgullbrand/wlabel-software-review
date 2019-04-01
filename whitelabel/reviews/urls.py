from django.urls import path
from .views import HomeView, CategoriesView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('categories/', CategoriesView.as_view(), name = 'categories'), 
    path('software_products/', views.software_products, name = 'software_products')
]
