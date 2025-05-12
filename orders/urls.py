from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('track_orders',views.track_order,name='track_page'),
    path('<int:id>',views.order_detail,name='detail_page')
]
