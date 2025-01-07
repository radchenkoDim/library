from django.urls import path

from . import views

urlpatterns = [
    path("table/", views.table, name="table"),
    path("how_take/", views.how_take, name="how_take"),
    path("table/<int:book_num>/", views.book, name="book"),
]