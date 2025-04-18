from django.shortcuts import render
from django.views import View 
from .models import Product
# Create your views here.


class Home(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'home.html',{'prods':products})
 