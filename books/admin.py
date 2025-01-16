from django.contrib import admin
from .models import Category, Publisher, Book

# Налаштування для Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для відображення у списку
    search_fields = ('name',)  # Додавання пошуку за назвою
    ordering = ('name',)  # Сортування за назвою


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']


# Налаштування для Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'author', 'category', 'year', 'tom', 'quantity', 'publisher', 'notes')  # Поля для списку
    search_fields = ('title', 'author', 'publisher', 'notes')  # Додавання пошуку за текстовими полями
    list_filter = ('category', 'year', 'publisher')  # Додавання фільтрів за полями
    ordering = ('num', )  

    # Секції для редагування полів
    fieldsets = (
        ('Основна інформація', {
            'fields': ('num', 'title', 'author', 'category', 'subcategory')
        }),
        ('Додаткові дані', {
            'fields': ('year', 'tom', 'publisher', 'notes')
        }),
    )

    # Поля для автозаповнення
    autocomplete_fields = ['category', 'publisher']

    # Додавання кастомної дії
    actions = ['mark_as_classic']

    @admin.action(description='Позначити книги як класичні (до 2000 року)')
    def mark_as_classic(self, request, queryset):
        queryset.update(notes='Classic')  # Оновлення поля notes для вибраних записів
