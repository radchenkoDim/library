from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms

from datetime import datetime
from dateutil.relativedelta import relativedelta

from books.models import Book
from .models import TakingBook

# Create your views here.
class TakeBookForm(forms.Form):
    num = forms.IntegerField(label="Номер")
    name = forms.CharField(label='Імʼя', max_length=100)
    surname = forms.CharField(label='Прізвище', max_length=100)
    telegram = forms.CharField(label='Telegram', max_length=100)

    # def take_book(self):
    #     book_id = self.cleaned_data['book_id']
    #     user_id = self.cleaned_data['user_id']
    #     take_date = self.cleaned_data['take_date']
    #     return_date = self.cleaned_data['return_date']
    #     book = get_object_or_404(Book, id=book_id)

def take_book(request):
    if request.method == 'POST':
        form = TakeBookForm(request.POST)
        if form.is_valid():
            book = get_object_or_404(Book, num=form.cleaned_data['num'])
            taking_book = TakingBook.objects.create(
                book=book,
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                telegram=form.cleaned_data['telegram'],
            )
            return HttpResponseRedirect(reverse('take_book:detail', args=(taking_book.id,)))
    else:
        initial = {}
        if 'book_num' in request.GET:
            book = get_object_or_404(Book, num=request.GET['book_num'])
            initial['num'] = book.num

        form = TakeBookForm(initial=initial)

    return render(request, 'take_book/take_book.html', {
        'form': form,
    })

def detail(request, taking_book_id):
    taking_book = get_object_or_404(TakingBook, id=taking_book_id)
    return_date = taking_book.take_date + relativedelta(months=1)
    return render(request, 'take_book/detail.html', {
        'taking_book': taking_book,
        'return_date': return_date,
    })

