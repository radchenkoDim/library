from . import views
from django.urls import path, include
from .views import register

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_profile, name='edit_profile'),
]