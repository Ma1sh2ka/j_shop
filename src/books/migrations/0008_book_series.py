# Generated by Django 3.2.3 on 2021-06-19 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0007_remove_author_picture'),
        ('books', '0007_alter_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='seriess', to='spravochniki.series'),
            preserve_default=False,
        ),
    ]
