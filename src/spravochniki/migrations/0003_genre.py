# Generated by Django 3.2.3 on 2021-05-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0002_auto_20210527_0244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Жанр')),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]