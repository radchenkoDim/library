# Generated by Django 5.1.5 on 2025-01-15 09:12

from django.db import migrations


def delete_data(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Book.objects.all().delete()
    Category = apps.get_model("books", "Category")
    Category.objects.all().delete()
    Subcategory = apps.get_model("books", "Subcategory")
    Subcategory.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_author_alter_book_notes_and_more'),
    ]

    operations = [
        migrations.RunPython(delete_data),
    ]
