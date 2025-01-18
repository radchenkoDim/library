from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import UserCreationForm
from .forms import UserChengeForm
from take_book.models import TakingBook
from users.models import User
from dateutil.relativedelta import relativedelta
from datetime import datetime
from django.contrib.auth.views import LoginView


def is_admin(user):
    return user.is_staff


@login_required
def profile_own(request):
    taking_books = TakingBook.objects.filter(user=request.user, return_date__isnull=True).order_by('take_date')
    username = request.user.username
    return render(request, "users/profile.html", {"taking_books": taking_books, "username": username})


@user_passes_test(is_admin)
def profile_user(request, user_id):
    taking_books = TakingBook.objects.filter(user=user_id).order_by('return_date')
    user_n = get_object_or_404(User, id=user_id)
    return render(request, "users/profile_user.html", {"user_n": user_n, "taking_books": taking_books})


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