from django.urls import path
from . import views

app_name = 'e_books'
urlpatterns = [
    path('', views.e_table, name='e_table'),
]
