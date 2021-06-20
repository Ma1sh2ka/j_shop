from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=150
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )
    

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('spravochniki:author', args=[self.pk])

class Meta:
    verbose_name = 'Автор'
    verbose_name_plural = 'Авторы'


class Series(models.Model):
    name = models.CharField(
        verbose_name='Серия',
        max_length=100,
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('spravochniki:series', args=[self.pk])

class Meta:
    verbose_name = 'Серия'
    verbose_name_plural = 'Серии'


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('spravochniki:genre', args=[self.pk])

class Meta:
    verbose_name = 'Жанр'
    verbose_name_plural = 'Жанры'


class Publishing_house(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length=100
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True
    )

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('spravochniki:publishing_house', args=[self.pk])

class Meta:
    verbose_name = 'Издательство'
    verbose_name_plural = 'Издательства'