from users.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


# Create your views here.
def hello(request):
    return render(request, "users/test.html")

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