# Generated by Django 4.2 on 2023-04-09 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Rat', '0003_remove_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default=0, max_length=800),
            preserve_default=False,
        ),
    ]