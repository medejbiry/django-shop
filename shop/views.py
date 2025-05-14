from django.shortcuts import render,get_object_or_404
from products.models import Category,Product

def Home_page(request) :
    category = Category.objects.all()
    products = Product.objects.all().order_by('created_at')[:5]
    return render(request,'Home.html',{'categories':category,'products':products})