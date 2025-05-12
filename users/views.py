from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.models import User


# Create your views here.

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('products:list')
    else:
        form = UserCreationForm()
    return render(request,'users/register.html',{ "form" : form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Check if the user is an employee
            if hasattr(user, 'is_superuser') and user.is_superuser == 1:
                # Redirect to a special employee dashboard or page
                return redirect('employee:dashboard')  # change to your desired view name
            elif 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('products:list')
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {"form": form})
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("products:list")