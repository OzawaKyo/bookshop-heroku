# Generated by Django 4.2 on 2023-04-09 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Rat', '0004_book_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
    ]
