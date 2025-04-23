from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.product_list,name='list'),
    path('<int:id>/',views.product_page,name = 'page'),
    path('category/<slug:slug>/',views.product_categorie,name='cat')
]
