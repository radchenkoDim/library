# Generated by Django 5.1.5 on 2025-01-22 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('take_book', '0003_wantbook_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wantbook',
            old_name='vote',
            new_name='votes',
        ),
    ]
