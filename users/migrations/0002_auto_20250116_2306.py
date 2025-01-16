# Generated by Django 5.1.5 on 2025-01-16 21:06

from django.db import migrations
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    User = get_user_model()
    User.objects.create_superuser(
        username='radchenkoDim',
        email='radchenko.dim@gmail.com',
        password='admin123'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
