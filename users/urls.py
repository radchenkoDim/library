from . import views
from django.urls import path, include
from .views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('hello/', views.hello, name='hello'),
    path('profile/', views.profile, name='profile'),
    path('register/', Register.as_view(), name='register'),
]