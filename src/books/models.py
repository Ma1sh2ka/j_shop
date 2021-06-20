from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=300
    )
    picture = models.ImageField(
        verbose_name='Фото обложки',
        upload_to='book/%Y/%m/%d/'
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=7,
        decimal_places=2
    )
    author = models.ManyToManyField(
        'spravochniki.Author',
        related_name='authors'
    
    )
    series = models.ForeignKey(
        'spravochniki.Series',
        on_delete=models.PROTECT,
        related_name='seriess'
    )
    genre = models.ManyToManyField(
        'spravochniki.Genre',
        related_name='genres'
    )
    year_publication = models.IntegerField(
        verbose_name='Год издания'
    )
    pages = models.IntegerField(
        verbose_name='Количество страниц'
    )
    binding = models.CharField(
        verbose_name='Переплет',
        max_length=100
    )
    format_book = models.CharField(
        verbose_name='Формат книги',
        max_length=100
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=20
    )
    weight = models.IntegerField(
        verbose_name='Вес книги'
    )
    age_limit = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=50
    )
    publishing_house = models.ForeignKey(
        'spravochniki.Publishing_house',
        on_delete=models.PROTECT,
        related_name='publishing_houses'
    )
    amount_available_books = models.IntegerField(
        verbose_name='Количество книг в наличии'
    )
    active = models.BooleanField(
        verbose_name='Доступна для заказа',
        default=False
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг'
    )
    created = models.DateTimeField(
        verbose_name='Дата внесения в каталог',
        auto_now=False,
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата последнего изменения',
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('books:book', args=[self.pk])

class Meta:
    verbose_name = 'Книга'
    verbose_name_plural = 'Книги'