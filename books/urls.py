from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table/", views.table, name="table"),
    path("table/<int:book_num>", views.book, name="book"),
    path("log_in/", views.log_in, name="log_in")
]