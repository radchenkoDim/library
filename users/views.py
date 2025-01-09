from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import UserCreationForm
from .forms import UserChengeForm
from take_book.models import TakingBook
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.contrib.auth.views import LoginView


@login_required
def profile(request):
    taking_books = TakingBook.objects.filter(user=request.user, return_date__isnull=True).order_by('take_date')

    # def i_am(one_book):
    #     return one_book.user == request.user
    
    # books = filter(lambda x: x.user == request.user, books)
    # books = filter(i_am, books)
    # # for i in books:
    # #     print(i)
    return render(request, "users/profile.html", {"taking_books": taking_books})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user 

    if request.method == 'POST':
        form = UserChengeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профіль успішно оновлено.')
            return redirect('profile')
    else:
        form = UserChengeForm(instance=user)

    return render(request, 'registration/edit_profile.html', {'form': form})