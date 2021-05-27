from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class Publishing_houseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Series, SeriesAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publishing_house, Publishing_houseAdmin)