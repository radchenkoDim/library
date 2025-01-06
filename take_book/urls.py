from django.urls import path
from . import views

app_name = 'take_book'
urlpatterns = [
    path('<int:book_id>/', views.take_book, name='take_book'),
    path('detail/<int:taking_book_id>/', views.detail, name='detail'),
]