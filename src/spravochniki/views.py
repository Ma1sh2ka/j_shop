from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from . import models
from . import forms

# Create your views here.

class AuthorDetailView(DetailView):
    model = models.Author

class AuthorListView(ListView):
    model = models.Author

class AuthorCreateView(CreateView):
    model = models.Author
    form_class = forms.CreateAuthorForm

class AuthorUpdateView(UpdateView):
    model = models.Author
    form_class = forms.CreateAuthorForm

class AuthorDeleteView(DeleteView):
    model = models.Author
    success_url = reverse_lazy('spravochniki:author-list')


class SeriesDetailView(DetailView):
    model = models.Series

class SeriesListView(ListView):
    model = models.Series

class SeriesCreateView(CreateView):
    model = models.Series
    form_class = forms.CreateSeriesForm

class SeriesUpdateView(UpdateView):
    model = models.Series
    form_class = forms.CreateSeriesForm

class SeriesDeleteView(DeleteView):
    model = models.Series
    success_url = reverse_lazy('spravochniki:series-list')


class GenreDetailView(DetailView):
    model = models.Genre

class GenreListView(ListView):
    model = models.Genre

class GenreCreateView(CreateView):
    model = models.Genre
    form_class = forms.CreateGenreForm

class GenreUpdateView(UpdateView):
    model = models.Genre
    form_class = forms.CreateGenreForm

class GenreDeleteView(DeleteView):
    model = models.Genre
    success_url = reverse_lazy('spravochniki:genre-list')


class Publishing_houseDetailView(DetailView):
    model = models.Publishing_house

class Publishing_houseListView(ListView):
    model = models.Publishing_house

class Publishing_houseCreateView(CreateView):
    model = models.Publishing_house
    form_class = forms.CreatePublishing_houseForm

class Publishing_houseUpdateView(UpdateView):
    model = models.Publishing_house
    form_class = forms.CreatePublishing_houseForm

class Publishing_houseDeleteView(DeleteView):
    model = models.Publishing_house
    success_url = reverse_lazy('spravochniki:publishing_house-list')


class Home(TemplateView):
    template_name = 'spravochniki/home.html'