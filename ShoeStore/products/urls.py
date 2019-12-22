from django.urls import path
from .views import ProductListView, product_list_view

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products-fbv/', product_list_view, name='products-fbv'),
]
