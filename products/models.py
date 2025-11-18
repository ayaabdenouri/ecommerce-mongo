from django.db import models
from djongo import models as djongo_models

class Category(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name

class Product(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)

    class Meta:
        abstract = False

    def __str__(self):
        return self.name
