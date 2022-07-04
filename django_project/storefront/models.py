from django.db import models

from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField('date added')
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
