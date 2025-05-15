from django.urls import path 
from . import views

urlpatterns=[
    path('api/products/',views.ProductListAPIView.as_view(),name='productlist'),
    path('api/products/<int:pk>/',views.ProductListAPIView.as_view(), name='product-detail'),


]
