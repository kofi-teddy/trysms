# Generated by Django 3.2.6 on 2021-08-11 19:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Buyers',
            new_name='Buyer',
        ),
    ]
