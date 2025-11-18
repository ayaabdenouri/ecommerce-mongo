from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from djongo import models as djongo_models

class Order(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.FloatField(default=0)
    status = models.CharField(max_length=50, default='En attente')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = False

class OrderItem(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        abstract = False
