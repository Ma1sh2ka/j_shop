# Generated by Django 3.2.3 on 2021-06-19 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spravochniki', '0007_remove_author_picture'),
        ('books', '0016_auto_20210619_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='publishing_houses', to='spravochniki.publishing_house'),
            preserve_default=False,
        ),
    ]