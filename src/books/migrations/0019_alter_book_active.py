# Generated by Django 3.2.3 on 2021-06-19 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0018_book_amount_available_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Доступна для заказа'),
        ),
    ]
