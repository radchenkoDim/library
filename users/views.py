from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, "users/test.html")

def profile(request):
    return render(request, "users/profile.html")