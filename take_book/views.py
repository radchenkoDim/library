from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from dateutil.relativedelta import relativedelta

from books.models import Book
from .models import TakingBook
from .forms import TakeBookForm, ReturnBookForm
from django.utils.timezone import now


@login_required
def take_book(request):
    book_title = None
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
            book_title = f"{book.num}. {book.title}"
        
        form = TakeBookForm(initial=initial)
    
    return render(request, 'take_book/take_book.html', {'form': form, 'book': book_title})


@login_required
def return_book(request):
    book = None
    initial = {}

    if request.method == 'POST':
        form = ReturnBookForm(request.POST, user=request.user)
        if form.is_valid():
            book_num = form.cleaned_data['book_num']
            
            taking_books = TakingBook.objects.filter(book__num=book_num, return_date__isnull=True)
            taking_book = taking_books.first()
            taking_book.return_date = now()
            taking_book.save()
            return redirect('take_book:success_return', taking_book_id=taking_book.id)
    else:
        if 'book_num' in request.GET:
            book = get_object_or_404(Book, num=request.GET['book_num'])
            initial['book_num'] = book.num

        form = ReturnBookForm(initial=initial)

    return render(request, 'take_book/return_book.html', {'form': form, 'book': book})


def success_return(request, taking_book_id):
    taking_book = get_object_or_404(TakingBook, id=taking_book_id)
    return render(request, 'take_book/success_return.html', {'taking_book': taking_book})
            

def detail(request, taking_book_id):
    taking_book = get_object_or_404(TakingBook, id=taking_book_id)
    need_to_return_date = taking_book.take_date + relativedelta(months=1)
    return render(request, 'take_book/detail.html', {
        'taking_book': taking_book,
        'need_to_return_date': need_to_return_date,
    })
