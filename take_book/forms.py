from django import forms
from .models import TakingBook

class TakeBookForm(forms.Form):
    book_num = forms.IntegerField(label="Номер книги")

    def clean_book_num(self):
        book_num = self.cleaned_data['book_num']
        taking_books = TakingBook.objects.filter(book__num=book_num, return_date__isnull=True)
        if not taking_books:
            raise forms.ValidationError(f'Книги з номером {book_num} немає в бібліотеці.')


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