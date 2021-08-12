from django.db import models
from django.db.models.fields import PositiveIntegerField

from apps.cars.models import Car



class Order(models.Model):
    name = models.CharField(max_length=255) 
    cars = models.ManyToManyField(Car)
    total = PositiveIntegerField(blank=True, null=True)
    total_price = PositiveIntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

