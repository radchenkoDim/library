from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'telegram_tag')
    search_fields = ('username', 'email', 'role', 'telegram_tag')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональна інформація', {'fields': ('first_name', 'last_name', 'email', 'telegram_tag')}),
        ('Роль користувача', {'fields': ('role',)}),
        ('Статус', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Дати', {'fields': ('last_login', 'date_joined')}),
        ('Додатково', {'fields': ('avatar', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'telegram_tag', 'password1', 'password2'),
        }),
    )
    ordering = ('username',)

admin.site.register(User, CustomUserAdmin)