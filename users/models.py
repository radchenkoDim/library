from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)  # Унікальний e-mail
    ROLE_CHOICES = [
        ('unknown', 'Не визначено'),
        ('7', '7 клас'),
        ('8', '8 клас'),
        ('9', '9 клас'),
        ('10', '10 клас'),
        ('11', '11 клас'),
        ('teacher', 'Викладач/Куратор'),
    ]
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES,
        default='unknown'
    )
    telegram_tag = models.CharField(max_length=100, blank=True, null=True)