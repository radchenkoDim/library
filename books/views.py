from django.shortcuts import render, get_object_or_404, redirect
from django.core.serializers import serialize
from books.models import Book
from .forms import AddBookForm
from take_book.models import WantBook
from django.contrib.admin.views.decorators import staff_member_required


def table(request):
    queryset = Book.objects.all().select_related("category").order_by("num") #.values("num", "title", "author", "category")
    json_data = serialize('json', queryset, use_natural_foreign_keys=True, fields=('num', 'title', 'author', 'category'))

    books_count = 0
    for book in queryset:
        books_count += book.quantity

    book_end = 'книга'
    if str(books_count)[-1] in ['2', '3', '4']:
        book_end = 'книги'
    elif str(books_count)[-1] in ['5', '6', '7', '8', '9', '0'] or str(books_count)[-2:] in ['11', '12', '13', '14']:
        book_end = 'книг'
    
    return render(request, "books/table.html", {
        "books": queryset,
        "books_json": json_data,
        "books_count": books_count,
        "book_end": book_end
    })


def book(request, book_num):
    book = get_object_or_404(Book, num=book_num)
    taked_by = book.takingbook_set.filter(return_date__isnull=True).values_list("user__username", flat=True)
    return render(request, "books/book.html", {
        "book": book,
        "publisher": book.publisher,
        "taked_by": taked_by
    })


@staff_member_required
def add_book(request):
    want_book = None
    if "want_book_id" in request.GET:
        want_book = get_object_or_404(WantBook, id=request.GET["want_book_id"])

    if request.method == "POST":
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            if want_book:
                want_book.status = "aproved"
                want_book.save()
            form.save()
            return redirect("index")
    else:
        initial = {"num": Book.get_free_num(),}
        if want_book:
            initial.update({
                "title": want_book.title,
                "author": want_book.author,
                "publisher": want_book.publisher,
            })
        form = AddBookForm(initial=initial)
    
    return render(request, "books/add_book.html", {"form": form})


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