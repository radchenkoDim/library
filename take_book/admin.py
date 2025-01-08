from django.contrib import admin
from .models import TakingBook

# Register your models here.
@admin.register(TakingBook)
class TakingBookAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'take_date', 'return_date',)
    list_filter = ('user', )