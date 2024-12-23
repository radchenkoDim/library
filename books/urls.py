from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("table/", views.table, name="table"),
    path("log_in/", views.log_in, name="log_in")
]