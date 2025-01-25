from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from dateutil.relativedelta import relativedelta

from books.models import Book
from .models import TakingBook, WantBook, Vote
from .forms import TakeBookForm, ReturnBookForm, WantBookForm
from django.utils.timezone import now
from django.contrib import messages
from utils import get_object_or_none


@login_required
def take_book(request):
    initial = {} 
    book = get_object_or_none(Book, num=request.GET.get('book_num'))

    if request.method == 'POST':
        form = TakeBookForm(request.POST)
        if form.is_valid():
            book_number = form.cleaned_data['book_num']
            taking_book = TakingBook.objects.create(
                user=request.user,
                book=Book.objects.get(num=book_number))
            
            return redirect('take_book:detail', taking_book_id=taking_book.id)
    else:
        if 'book_num' in request.GET:
            initial['book_num'] = book.num

        form = TakeBookForm(initial=initial)
    
    return render(request, 'take_book/take_book.html', {'form': form, 'book': book})


@login_required
def return_book(request):
    book = None

    if request.method == 'POST':
        form = ReturnBookForm(request.POST, user=request.user)
        if form.is_valid():
            book_num = form.cleaned_data['book_num']
            
            taking_books = TakingBook.objects.filter(book__num=book_num, return_date__isnull=True)
            taking_book = taking_books.first()
            taking_book.return_date = now()
            taking_book.save()

            messages.success(request, f'Книгу з номером {book_num} успішно повернено.')
            return redirect('profile')
    else:
        if 'book_num' in request.GET:
            book = get_object_or_404(Book, num=request.GET['book_num'])

        form = ReturnBookForm()

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


@login_required
def want_book(request):
    books = WantBook.objects.all()
    voted_books = []

    if request.user.is_authenticated:
        voted_books = Vote.objects.filter(user=request.user).values_list('want_book_id', flat=True)

    return render(request, 'take_book/want_book.html', {
        'books': books, 
        'voted_books': voted_books
    })


@login_required
def vote(request, want_book_id):
    want_book = get_object_or_404(WantBook, id=want_book_id)

    if want_book.user == request.user:
        return redirect('take_book:want_book')
    
    if Vote.objects.filter(user=request.user, want_book=want_book).exists():
        return redirect('take_book:want_book')
    
    Vote.objects.create(user=request.user, want_book=want_book)
    want_book.votes += 1
    want_book.save()

    return redirect('take_book:want_book')


def voted_book(request, want_book_id):
    want_book = get_object_or_404(WantBook, id=want_book_id)
    voted_users = Vote.objects.filter(want_book=want_book)
    users = [vote.user for vote in voted_users]
    return render(request, 'take_book/voted_book.html', {
        'book': want_book, 
        'users': users
    })


@login_required
def want_book_form(request):
    if request.method == 'POST':
        form = WantBookForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('take_book:want_book_success')
    else:
        form = WantBookForm()
    
    return render(request, 'take_book/want_book_form.html', {'form': form})


@login_required
def want_book_success(request):
    return render(request, 'take_book/want_book_success.html')


@login_required
def taking_books(request):
    taking_books = TakingBook.objects.filter(return_date__isnull=True).order_by('take_date')
    return render(request, 'take_book/taking_books.html', {'books': taking_books})