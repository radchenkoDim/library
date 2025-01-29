from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from books.models import Book
from django.core.serializers import serialize


def book_item(request, book_num):
    queryset = Book.objects.filter(num=book_num)
    if not queryset.exists():
        return HttpResponse(status=404)
    # book = get_object_or_404(Book, num=book_num)
    json_data = serialize('json', queryset, use_natural_foreign_keys=True, fields=('num', 'title', 'author', 'category'))
    return HttpResponse(json_data, content_type='application/json')