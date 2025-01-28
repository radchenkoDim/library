from django.contrib import admin
from .models import Category, Publisher, Book
from django.db.models import Max

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
    list_display = ('num', 'title', 'author', 'category', 'year', 'tom', 'quantity', 'publisher')  # Поля для списку
    search_fields = ('title', 'author', 'publisher__name', 'notes')  # Додавання пошуку за текстовими полями
    list_filter = ('category', 'publisher', 'year')  # Додавання фільтрів за полями
    ordering = ('num', )  

    # Секції для редагування полів
    fieldsets = (
        ('Основна інформація', {
            'fields': ('num', 'title', 'author', 'category')
        }),
        ('Додаткові дані', {
            'fields': ('cover', 'year', 'tom', 'quantity', 'publisher', 'notes')
        }),
    )

    # Поля для автозаповнення
    autocomplete_fields = ['category', 'publisher']

    # Додавання початкових значень
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['num'].initial = Book.get_next_num()
        return form

    # Додавання кастомної дії
    actions = ['mark_as_classic']
