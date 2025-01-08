from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

from datetime import datetime
from dateutil.relativedelta import relativedelta

from books.models import Book
from users.models import User
from .models import TakingBook
from .forms import TakeBookForm

# Create your views here.
# def take_book(request):
#     book_global = None
#     if request.method == 'POST':
#         form = TakeBookForm(request.POST)
#         if form.is_valid():
#             book = get_object_or_404(Book, num=form.cleaned_data['num'])
#             taking_book = TakingBook.objects.create(
#                 book=book,
#                 name=form.cleaned_data['name'],
#                 surname=form.cleaned_data['surname'],
#                 telegram=form.cleaned_data['telegram'],
#             )
#             return HttpResponseRedirect(reverse('take_book:detail', args=(taking_book.id,)))
#     else:
#         initial = {}
#         if 'book_num' in request.GET:
#             book = get_object_or_404(Book, num=request.GET['book_num'])
#             initial['num'] = book.num
#             book_global = book.title

#         form = TakeBookForm(initial=initial)
#     return render(request, 'take_book/take_book.html', {
#         'form': form,
#         'book': book_global,
#     })

# class TakeBookForm(forms.Form):
#     book_num = forms.IntegerField(label="Номер книги")
#     username = forms.CharField(label='Username', max_length=100)

@login_required
def take_book(request):
    book_global = None
    initial = {} 
    
    if request.method == 'POST':
        form = TakeBookForm(request.POST)
        if form.is_valid():
            book_number = form.cleaned_data['book_num']
            user = request.user

            taking_book = TakingBook.objects.create(
                user=user,
                book=Book.objects.get(num=book_number),
            )
            return redirect('take_book:detail', taking_book_id=taking_book.id)
    else:
        if 'book_num' in request.GET:
            book = get_object_or_404(Book, num=request.GET['book_num'])
            initial['book_num'] = book.num
            book_global = f"{book.num}. {book.title}"
        
        form = TakeBookForm(initial=initial)
    
    return render(request, 'take_book/take_book.html', {'form': form, 'book': book_global})

                
def detail(request, taking_book_id):
    taking_book = get_object_or_404(TakingBook, id=taking_book_id)
    need_to_return_date = taking_book.take_date + relativedelta(months=1)
    return render(request, 'take_book/detail.html', {
        'taking_book': taking_book,
        'need_to_return_date': need_to_return_date,
    })
