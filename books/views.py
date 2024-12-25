from django.shortcuts import render
from django.core.serializers import serialize
from .models import Book
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, "books/index.html", {
        "books": Book.objects.all().count()
    })

def table(request):
    queryset = Book.objects.all().select_related("category", "subcategory")
    json_data = serialize('json', queryset, use_natural_foreign_keys=True)
    return render(request, "books/table.html", {
        "books": queryset,
        "books_json": json_data
    })

def book(request, book_num):
    book = Book.objects.filter(num=book_num)
    return render(request, "books/book.html", {
        "book": book
    })