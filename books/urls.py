from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("table/", views.table, name="table"),
    path("table/<int:book_num>/", views.book, name="book"),
    path("table/category/<str:category_name>/", views.category, name="category"),
    path("table/publisher/<str:publisher_name>/", views.publisher, name="publisher"),
    path("work/", views.work, name="work"),
]