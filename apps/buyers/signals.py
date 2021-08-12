from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import CustomUser as User
from .models import Buyer

@receiver(post_save, sender=User)
def post_save_create_buyer(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if created:
        Buyer.objects.create(user=instance)
    pass
