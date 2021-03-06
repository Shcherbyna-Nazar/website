from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=201)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    product_photo = models.ImageField(null=True, default="/images/kohala-full-size-steel-string-acoustic-guitar.jpg", upload_to='images/')

    # product_owner = models.ForeignKey(User, on_delete=models.Cascade)
    def __str__(self):
        return f'{self.name} with price {self.price}'
