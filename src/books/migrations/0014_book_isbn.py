# Generated by Django 3.2.3 on 2021-06-19 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_book_format_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(default=1, verbose_name='ISBN'),
            preserve_default=False,
        ),
    ]
