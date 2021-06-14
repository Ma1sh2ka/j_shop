from django.urls import path

from spravochniki import views as spravochniki_views
app_name = 'spravochniki'

urlpatterns = [
    path('author/<int:pk>/', spravochniki_views.AuthorDetailView.as_view(), name='author'),
    path('authors', spravochniki_views.AuthorListView.as_view(), name='author-list'),
    path('series/<int:pk>/', spravochniki_views.SeriesDetailView.as_view(), name='series'),
    path('seriess', spravochniki_views.SeriesListView.as_view(), name='series-list'),
    path('genre/<int:pk>/', spravochniki_views.GenreDetailView.as_view(), name='genre'),
    path('genres', spravochniki_views.GenreListView.as_view(), name='genre-list'),
    path('publishing_house/<int:pk>/', spravochniki_views.Publishing_houseDetailView.as_view(), name='publishing_house'),
    path('publishing_houses', spravochniki_views.Publishing_houseListView.as_view(), name='publishing_house-list'),
    path('create-author/', spravochniki_views.AuthorCreateView.as_view(), name='author_create'),
    path('update-author/<int:pk>/', spravochniki_views.AuthorUpdateView.as_view(), name='author_update'),
    path('delete-author/<int:pk>/', spravochniki_views.AuthorDeleteView.as_view(), name='author_delete'),
    path('create-series/', spravochniki_views.SeriesCreateView.as_view(), name='series_create'),
    path('update-series/<int:pk>/', spravochniki_views.SeriesUpdateView.as_view(), name='series_update'),
    path('delete-series/<int:pk>/', spravochniki_views.SeriesDeleteView.as_view(), name='series_delete'),
    path('create-genre/', spravochniki_views.GenreCreateView.as_view(), name='genre_create'),
    path('update-genre/<int:pk>/', spravochniki_views.GenreUpdateView.as_view(), name='genre_update'),
    path('delete-genre/<int:pk>/', spravochniki_views.GenreDeleteView.as_view(), name='genre_delete'),
    path('create-publishing_house/', spravochniki_views.Publishing_houseCreateView.as_view(), name='publishing_house_create'),
    path('update-publishing_house/<int:pk>/', spravochniki_views.Publishing_houseUpdateView.as_view(), name='publishing_house_update'),
    path('delete-publishing_house/<int:pk>/', spravochniki_views.Publishing_houseDeleteView.as_view(), name='publishing_house_delete')
]