from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    city = models.TextField()
    address = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered')
    ])



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
