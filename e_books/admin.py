from django.contrib import admin
from .models import EBook


@admin.register(EBook)
class EBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author')  # Поля для списку
    search_fields = ('title', 'author')  # Додавання пошуку за текстовими полями

    # Секції для редагування полів
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'author', 'category')
        }),
        ('Додаткові дані', {
            'fields': ('file',)
        }),
    )