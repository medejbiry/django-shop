from django.shortcuts import render,get_object_or_404,redirect
from .models import Order,OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='users:login')
def track_order(request):
    orders = Order.objects.filter(user = request.user)
    return render(request,'order/track_orders.html',{"orders":orders})

def order_detail(request,id):
    order = get_object_or_404(Order,id = id)
    orderItems = OrderItem.objects.filter(order = order)
    return render(request,'order/order_detail_page.html',{'order':order,'orderItems':orderItems})