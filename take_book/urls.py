from django.urls import path
from . import views

app_name = 'take_book'
urlpatterns = [
    path('', views.take_book, name='take_book'),
    path('detail/<int:taking_book_id>/', views.detail, name='detail'),
    path('return_book/', views.return_book, name='return_book'),
    path('success_return/<int:taking_book_id>/', views.success_return, name='success_return'),
]