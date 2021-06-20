from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from . import models
from . import forms

# Create your views here.

class BookDetailView(DetailView):
    model = models.Book

class BookListView(ListView):
    model = models.Book

class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.CreateBookForm

class BookUpdateView(UpdateView):
    model = models.Book
    form_class = forms.CreateBookForm

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy('books:book-list')


class Home(TemplateView):
    template_name = 'spravochniki/home.html'