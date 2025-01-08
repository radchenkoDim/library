from django import forms

class TakeBookForm(forms.Form):
    book_num = forms.IntegerField(label="Номер книги")
    username = forms.CharField(label='Username', max_length=100)

class ReturnBookForm(forms.Form):
    pass