from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from .models import Book

# Create your views here.
def table(request):
    queryset = Book.objects.all().select_related("category")
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


def category(request, category_name):
    queryset = Book.objects.filter(category__name=category_name).all()
    json_data = serialize('json', queryset, use_natural_foreign_keys=True)
    return render(request, "books/category.html", {
        "category": category_name,
        "books": queryset,
        "books_json": json_data
    })


def publisher(request, publisher_name):
    queryset = Book.objects.filter(publisher=publisher_name).all()
    print(queryset)
    return render(request, "books/publisher.html", {
        "publisher": publisher_name,
        "books": queryset
    })


def work(request):
    return render(request, "work.html")