from django.urls import path 
from . import views

urlpatterns=[
    path('',views.Home.as_view(),name='home'), 
    path('prodcreate/',views.ProductCreate.as_view(),name='productcreate'),

]
