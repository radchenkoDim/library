from django.contrib import admin
from .models import Category, Subcategory, Book

# Налаштування для Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для відображення у списку
    search_fields = ('name',)  # Додавання пошуку за назвою
    ordering = ('name',)  # Сортування за назвою
    

# Налаштування для Subcategory
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')  # Відображення полів
    search_fields = ('name', 'category__name')  # Пошук за підкатегорією та категорією
    list_filter = ('category',)  # Фільтри за категорією
    ordering = ('category', 'name')  # Сортування за категорією та назвою


# Налаштування для Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('num', 'title', 'author', 'category', 'subcategory', 'year', 'publisher', 'notes')  # Поля для списку
    search_fields = ('title', 'author', 'publisher', 'notes')  # Додавання пошуку за текстовими полями
    list_filter = ('category', 'subcategory', 'year', 'publisher')  # Додавання фільтрів за полями
    ordering = ('-year', 'title')  # Сортування за роком (спадаюче) та назвою

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
    autocomplete_fields = ['category', 'subcategory']

    # Додавання кастомної дії
    actions = ['mark_as_classic']

    @admin.action(description='Позначити книги як класичні (до 2000 року)')
    def mark_as_classic(self, request, queryset):
        queryset.update(notes='Classic')  # Оновлення поля notes для вибраних записів
