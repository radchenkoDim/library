from django.db import models
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
import os


class EBook(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey('books.Category', null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=255)
    file = models.FileField(upload_to='e_books')

    def __str__(self):
        return self.title