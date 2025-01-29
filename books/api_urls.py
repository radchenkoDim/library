from django.urls import path

from . import views
from . import api_views as api

urlpatterns = [
    path("item/<int:book_num>/", api.book_item, name="api_book_item"),
]