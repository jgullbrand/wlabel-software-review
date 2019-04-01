from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'), #home page
    path('categories/', views.categories, name = 'categories'), #list of categories
    path('software_products/', views.software_products, name = 'software_products'),
    path('profile/', views.profile, name = 'profile')
]
