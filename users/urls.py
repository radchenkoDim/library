from . import views
from django.urls import path, include
from .views import register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('hello/', views.hello, name='hello'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
]