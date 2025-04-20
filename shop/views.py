from django.shortcuts import render,get_object_or_404
from products.models import Category

def Home_page(request) :
    category = Category.objects.all()
    return render(request,'Home.html',{'categories':category})