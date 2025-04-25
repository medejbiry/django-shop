from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product

# Create your views here.


def add_to_cart(request):
    if request.method == 'POST': 
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product,id =product_id)
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )
        if not created:

            cart_item.save()

        return redirect('products:list')

        # if test_value:  # check if it's not empty
        #     cart_item = CartTest(name=test_value)
        #     cart_item.save()
    else:
        return render(request, 'cart_page.html')

def remove_item_from_cart(request,id):
    item = get_object_or_404(CartItem, id = id)
    item.delete()
    return redirect("cart:page")

@login_required(login_url='users:login')
def cart_page(request):
    cartItems = CartItem.objects.filter(user = request.user)
    return render(request , 'cart_page.html',{'cartItems':cartItems})