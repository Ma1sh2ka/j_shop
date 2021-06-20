# Generated by Django 3.2.3 on 2021-06-19 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0007_remove_author_picture'),
        ('books', '0008_book_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='genres', to='spravochniki.Genre'),
        ),
    ]