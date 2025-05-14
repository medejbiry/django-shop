from django.shortcuts import render,get_object_or_404,redirect
from orders.models import Order,OrderItem
from django.contrib import messages
# Create your views here.

def dashboard(request):
    order = Order.objects.all()

    return render(request,'employee/base.html',{'orders':order})

def order_detail(request,id):
    order = get_object_or_404(Order,id = id)
    orderItems = OrderItem.objects.filter(order = order)
    print(orderItems)
    return render(request,'employee/order_detail_em.html',{'order':order,'orderItems':orderItems})

def change_order_status(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in ["pending", "shipped", "delivered"]:
            order.status = new_status
            order.save()
            messages.success(request, f"Order status updated to {new_status}.")
        else:
            messages.error(request, "Invalid status.")
    return redirect("employee:dashboard")

def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    messages.success(request, "Order deleted successfully.")
    return redirect("employee:dashboard")  # redirect to your order list page