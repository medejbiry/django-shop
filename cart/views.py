from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem
from products.models import Product
from orders.models import Order,OrderItem

# Create your views here.

@login_required(login_url='users:login')
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
    else:
        return render(request, 'cart_page.html')
    
@login_required(login_url='users:login')
def remove_item_from_cart(request,id):
    item = get_object_or_404(CartItem, id = id)
    item.delete()
    return redirect("cart:page")

@login_required(login_url='users:login')
def cart_page(request):
    modified_cart_items = []
    cart_Total = 0
    cartItems = CartItem.objects.filter(user = request.user)
    for item in cartItems:
        total = item.quantity * item.product.price
        cart_Total = cart_Total + total
        modified_cart_items.append({
            'item' : item,
            'total' : total
        })
    return render(request , 'cart_page.html',{'cartItems':modified_cart_items,'total':cart_Total})

def add_order(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user = request.user)
        city = request.POST.get('city')
        adresse = request.POST.get('adresse')
        total = request.POST.get('total')
        order_container ,created = Order.objects.get_or_create(
            user = request.user,
            city = city,
            address = adresse,
            status = 'Pending'
        )
        if not created:
            order_container.save()
        
        for item in cart_items:
            order_item ,created = OrderItem.objects.get_or_create(
                order = order_container,
                product = item.product,
                quantity = item.quantity,
                price = item.product.price
            )
            if not created:
                order_item.save()
        return redirect("cart:page")
    return redirect("cart:page")


def increase_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity < item.product.stock:
        item.quantity += 1
        item.save()

    return redirect('cart:page')
@login_required
def decrease_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()
    return redirect('cart:page')
