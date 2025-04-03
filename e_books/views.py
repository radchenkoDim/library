from django.shortcuts import render
from .models import EBook
from django.core.serializers import serialize


def e_table(request):
    e_books = EBook.objects.all()
    json_data = serialize('json', e_books, use_natural_foreign_keys=True, fields=('title', 'author', 'category', 'file'))
    return render(request, 'e_books/e_table.html', {
        'e_books': e_books,
        'e_books_json': json_data
    })


