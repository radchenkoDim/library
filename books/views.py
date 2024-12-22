from django.shortcuts import render
from django.core.serializers import serialize
from .models import Book
import json

# Create your views here.
def index(request):
    return render(request, "books/index.html", {
        "books": Book.objects.all().count()
    })

def table(request):
    queryset = Book.objects.all()
    json_data = serialize('json', queryset, use_natural_foreign_keys=True)
    return render(request, "books/table.html", {
        "books": queryset,
        "books_json": json_data
    })

