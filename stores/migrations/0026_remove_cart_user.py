# Generated by Django 4.2.2 on 2024-02-23 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0025_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
