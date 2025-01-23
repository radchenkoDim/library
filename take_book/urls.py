from django.urls import path # type: ignore
from . import views

app_name = 'take_book'
urlpatterns = [
    path('', views.take_book, name='take_book'),
    path('detail/<int:taking_book_id>/', views.detail, name='detail'),
    path('return_book/', views.return_book, name='return_book'),
    path('success_return/<int:taking_book_id>/', views.success_return, name='success_return'),
    path('taking_books/', views.taking_books, name='taking_books'),
    path('want_book/', views.want_book, name='want_book'),
    path('vote/<int:want_book_id>/', views.vote, name='vote'),
    path('voted_book/<int:want_book_id>/', views.voted_book, name='voted_book'),
    path('want_book_form/', views.want_book_form, name='want_book_form'),
    path('want_book_form/want_book_success/', views.want_book_success, name='want_book_success'),
]