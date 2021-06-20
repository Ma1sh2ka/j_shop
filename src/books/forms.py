from django import forms
from . import models

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            'name',
            'picture',
            'price',
            'author',
            'series',
            'genre',
            'year_publication',
            'pages',
            'binding',
            'format_book',
            'isbn',
            'weight',
            'age_limit',
            'publishing_house',
            'amount_available_books',
            'active',
            'rating'
        )