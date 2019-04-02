from django.urls import path
from .views import HomeView, CategoryView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('<str:category_url>/', CategoryView.as_view(), name = 'categories'), 
]
