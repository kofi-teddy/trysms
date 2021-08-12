from django.db import models
from django.db.models.fields.related import OneToOneField

from apps.users.models import CustomUser


class Buyer(models.Model):
    user = OneToOneField(CustomUser, on_delete=models.CASCADE)
    from_signal = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.user}'