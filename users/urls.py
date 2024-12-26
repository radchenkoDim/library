from . import views
from django.urls import path, include

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('hello/', views.hello, name='hello'),
]