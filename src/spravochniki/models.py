from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        verbose_name='Автор',
        max_length=150
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self) -> str:
        return self.name

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
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Meta:
    verbose_name = 'Серия'
    verbose_name_plural = 'Серии'


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Жанр',
        max_length=100
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Meta:
    verbose_name = 'Жанр'
    verbose_name_plural = 'Жанры'


class Publishing_house(models.Model):
    name = models.CharField(
        verbose_name='Издательство',
        max_length=100
    )
    description = models.TextField(
        blank=True
    )

    def __str__(self) -> str:
        return self.name

class Meta:
    verbose_name = 'Издательство'
    verbose_name_plural = 'Издательства'