# Generated by Django 3.2.3 on 2021-06-19 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0006_author_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='picture',
        ),
    ]
