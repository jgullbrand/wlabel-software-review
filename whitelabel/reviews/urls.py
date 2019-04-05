from django.urls import path
from .views import HomeView, CategoryView, CreatePosting, ProductView, UpdatePosting, DeletePosting, CreateReview
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('results/', views.results, name='search_results'),
    path('product_listing/', CreatePosting.as_view(success_url='/'), name= "list_product"),
    path('<str:category_url>/', CategoryView.as_view(), name = 'categories'), 
    path('software_product/<int:pk>/', ProductView.as_view(), name = 'product-view'),
    path('software_product/<int:pk>/update/', UpdatePosting.as_view(), name = 'update_listing'),
    path('software_product/<int:pk>/delete/', DeletePosting.as_view(), name = 'delete_listing'),
    path('software_product/<int:pk>/review/', CreateReview.as_view(), name = 'create_review'),
]
