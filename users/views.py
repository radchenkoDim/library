from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import UserCreationForm
from .forms import UserChengeForm


# Create your views here.
# def hello(request):
#     return render(request, "users/test.html")

@login_required
def profile(request):
    return render(request, "users/profile.html")

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