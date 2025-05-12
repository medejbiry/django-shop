from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.cart_page,name='page'),
    path('add-to-cart',views.add_to_cart,name='add-to-cart'),
    path('<int:id>',views.remove_item_from_cart,name='remove-item'),
    path('order',views.add_order, name='order')
]
