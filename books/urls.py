from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("table/", views.table, name="table"),
    path("table/<int:book_num>/", views.book, name="book"),
]