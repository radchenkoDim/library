from django import forms

class TakeBookForm(forms.Form):
    book_num = forms.IntegerField(label="Номер книги")

class ReturnBookForm(forms.Form):
    book_num = forms.IntegerField(label="Номер книги")