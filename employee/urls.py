from django.urls import path
from . import views

app_name = 'employee'

urlpatterns= [
    path('',views.dashboard,name='dashboard'),
    path('<int:id>',views.order_detail,name='action'),
    path("<int:id>/change-status/", views.change_order_status, name="change_status"),
    path("<int:id>/delete/", views.delete_order, name="delete_order"),
    
]