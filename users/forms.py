from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import PasswordResetForm

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'telegram_tag', 'password1', 'password2']
        labels = {
            'username': 'Username',
            'first_name': 'Ім\'я',
            'last_name': 'Прізвище',
            'email': 'E-mail',
            'role': 'Роль',
            'telegram_tag': 'Тег в Telegram',
        }

    def clean_telegram_tag(self):
        telegram_tag = self.cleaned_data['telegram_tag']
        if telegram_tag and not telegram_tag.startswith('@'):
            raise ValidationError("Telegram tag must start with @.")
        return telegram_tag
        

class UserChengeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'role', 'telegram_tag']
        labels = {
            'email': 'E-mail',
            'role': 'Роль',
            'telegram_tag': 'Тег в Telegram',
        }


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='E-mail', max_length=254, widget=forms.EmailInput(attrs={'autocomplete': 'email'}))
    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise ValidationError("Користувача з таким e-mail не існує.")
        return email