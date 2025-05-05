from django.shortcuts import render
from django.views import View 
from django.http import HttpResponseRedirect
from .models import Product
from .forms import  ProductForm


class Home(View):
    def get(self,request):
        products=Product.objects.all()
        return render(request,'home.html',{'prods':products})
 

class ProductCreate(View):
    def get(self,request):
        form=ProductForm()
        return render(request,'createpro.html',{'form':form})
    def post(self,request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, 'createpro.html', {'form':form})
        
    
class Productupdate(View):
    def get(self,request):
        prod=Product.objects.get(id=id)
        form=ProductForm()
        return render(request,'productCreate.html',{'form':form})
    