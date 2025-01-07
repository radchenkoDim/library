from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from .models import Book

# Create your views here.
def table(request):
    queryset = Book.objects.all().select_related("category", "subcategory")
    json_data = serialize('json', queryset, use_natural_foreign_keys=True)
    return render(request, "books/table.html", {
        "books": queryset,
        "books_json": json_data
    })

def book(request, book_num):
    book = get_object_or_404(Book, num=book_num)
    return render(request, "books/book.html", {
        "book": book
    })

def how_take(request):
    return render(request, "books/how_take.html")