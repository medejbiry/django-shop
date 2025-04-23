from django.shortcuts import render,get_object_or_404
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all().order_by('created_at')
    return render(request , 'products/products_list.html',{'products':products})

def product_page(request , id):
    product = get_object_or_404(Product,id = id)
    return render(request , 'products/product_page.html',{"product":product})

def product_categorie(request,slug):
    products = Product.objects.filter(category__slug = slug)
    return render(request , 'products/products_list.html',{'products':products})
