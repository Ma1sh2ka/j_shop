from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'picture', 'price', 'active']

admin.site.register(models.Book, BookAdmin)