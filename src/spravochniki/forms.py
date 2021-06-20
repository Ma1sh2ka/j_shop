from django import forms
from . import models

class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'name',
            'description'
        )

class CreateSeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = (
            'name',
            'description'
        )

class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'name',
            'description'
        )

class CreatePublishing_houseForm(forms.ModelForm):
    class Meta:
        model = models.Publishing_house
        fields = (
            'name',
            'description'
        )