# Generated by Django 3.2.3 on 2021-06-19 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_book_isbn'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='weight',
            field=models.IntegerField(default=2, verbose_name='Вес книги'),
            preserve_default=False,
        ),
    ]