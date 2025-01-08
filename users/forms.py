from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

User = get_user_model()

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'telegram_tag', 'password1', 'password2']

    def clean_telegram_tag(self):
        telegram_tag = self.cleaned_data['telegram_tag']
        if telegram_tag and not telegram_tag.startswith('@'):
            raise ValidationError("Telegram tag must start with @.")
        return telegram_tag
        