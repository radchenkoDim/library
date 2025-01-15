from django.urls import path

from . import views

app_name = "books"
urlpatterns = [
    path("table/", views.table, name="table"),
    path("table/<int:book_num>/", views.book, name="book"),
    path("table/category/<str:category_name>/", views.category, name="category"),
    path("table/subcategory/<str:subcategory_name>/", views.subcategory, name="subcategory"),
    path("work/", views.work, name="work"),
]