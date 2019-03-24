from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'), #home page
    path('categories/', views.categories, ), #will software products based on category
    path('profile/', views.profile, name = 'profile')
]
