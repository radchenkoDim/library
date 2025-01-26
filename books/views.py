from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from books.models import Book


def table(request):
    queryset = Book.objects.all().select_related("category").order_by("-num") #.values("num", "title", "author", "category")
    json_data = serialize('json', queryset, use_natural_foreign_keys=True, fields=('num', 'title', 'author', 'category'))
    return render(request, "books/table.html", {
        "books": queryset,
        "books_json": json_data
    })


def book(request, book_num):
    book = get_object_or_404(Book, num=book_num)
    taked_by = book.takingbook_set.filter(return_date__isnull=True).values_list("user__username", flat=True)
    return render(request, "books/book.html", {
        "book": book,
        "publisher": book.publisher,
        "taked_by": taked_by
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
    books = Book.objects.filter(publisher__name=publisher_name)
    return render(request, "books/publisher.html", {
        "publisher": publisher_name,
        "books": books
    })


def author(request, author_name):
    books = Book.objects.filter(author=author_name)
    return render(request, "books/author.html", {
        "author": author_name,
        "books": books
    })


def work(request):
    return render(request, "work.html")