from users.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login


# Create your views here.
def hello(request):
    return render(request, "users/test.html")

def profile(request):
    return render(request, "users/profile.html")

class Register(View):

    template_names = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_names, context)
    
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        context = {
            'form': form
        }
        return render(request, self.template_names, context)