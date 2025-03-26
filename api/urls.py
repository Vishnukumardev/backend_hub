from django.urls import path
from api.views import *

urlpatterns = [
    # Example URL patterns
    # path('example/', views.example_view, name='example'),
    path('get_product/', get_product, name='get_product'),
    path('add_product/', manage_products, name='create_product'),
    path('update_product/', manage_products, name='update_product'),
    path('delete_product/', delete_product, name='delete_product'),
    path('list_products/', manage_products, name='list_products'),
]