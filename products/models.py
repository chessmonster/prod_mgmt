from django.urls import reverse
from django.db import models


class Product(models.Model):
    product_name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255)
    sku = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('products:detail', args=[str(self.id)])
