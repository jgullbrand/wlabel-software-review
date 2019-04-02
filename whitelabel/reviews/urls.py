from django.urls import path
from .views import HomeView, CategoryView, CreatePosting

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('product_listing/', CreatePosting.as_view(success_url='/'), name= "list_product"),
    path('<str:category_url>/', CategoryView.as_view(), name = 'categories'), 
]
