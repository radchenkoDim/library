from django.contrib import admin
from .models import TakingBook, WantBook

# Register your models here.
@admin.register(TakingBook)
class TakingBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'take_date', 'return_date',)
    list_filter = ('user', )


@admin.register(WantBook)
class WantBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'author', 'publisher', 'date', 'where',)
    list_filter = ('user', )