from django import forms
from .models import TakingBook, WantBook
from books.models import Book
from utils import get_object_or_none

class TakeBookForm(forms.Form):
    book_num = forms.IntegerField(label="Номер книги")

    def clean_book_num(self):
        book_num = self.cleaned_data['book_num']
        book = get_object_or_none(Book, num=book_num)
        if book is None:
            raise forms.ValidationError(f'Книги з номером {book_num} немає в бібліотеці.')
        taking_books_count = TakingBook.objects.filter(book=book, return_date__isnull=True).count()
        if taking_books_count >= book.quantity:
            raise forms.ValidationError(f'Книгу з номером {book_num} хтось вже взяв.')

        return book_num


class ReturnBookForm(forms.Form):
    book_num = forms.IntegerField(label="Номер книги")

    def __init__(self, *args, **kwargs):
        # Забираємо `user` із kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_book_num(self):
        book_num = self.cleaned_data['book_num']
        taking_books = TakingBook.objects.filter(book__num=book_num, return_date__isnull=True)
        if not taking_books:
            raise forms.ValidationError(f'Вами не було взято книгу з номером {book_num}, або такої книги немає в бібліотеці.')

        taking_book = taking_books.first()

        if taking_book.user != self.user:
            raise forms.ValidationError(f'Книгу з номером {book_num} взяв інший користувач.')

        return book_num
    

class WantBookForm(forms.Form):
    title = forms.CharField(label="Назва книги")
    author = forms.CharField(label="Автор")
    publisher = forms.CharField(label="Видавництво")
    where = forms.CharField(label="Де можна знайти")

    # class Meta:
    #     model = WantBook
    #     fields = ['title', 'author', 'publisher', 'where']

    # def save(self, user):
    #     want_book = super().save(commit=False)
    #     want_book.user = user
    #     want_book.save()
    #     return want_book
    