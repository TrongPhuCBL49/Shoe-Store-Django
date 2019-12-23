from django.urls import path
from .views import (
    ProductListView, 
    product_list_view, 
    ProductDetailView, 
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView,
    )

app_name = 'products'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products'),
    path('products-fbv/', product_list_view, name='products-fbv'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='products-detail'),
    path('products-fbv/<int:pk>', product_detail_view, name='products-fbv-detail'),
    path('feature-products/', ProductFeaturedListView.as_view(), name='feature-products'),
    path('feature-products/<int:pk>', ProductFeaturedDetailView.as_view(), name='feature-products-detail'),
    
]
