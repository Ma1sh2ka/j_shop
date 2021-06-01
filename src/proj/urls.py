"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# from cities import views as cities_views
from spravochniki import views as spravochniki_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('<code>/', cities_views.cities),
    # path('', cities_views.home),
    path('author/<int:author_id>/', spravochniki_views.author, name='author'),
    path('authors/', spravochniki_views.author_list, name='author-list'),
    path('series/<int:series_id>/', spravochniki_views.series, name='series'),
    path('seriess/', spravochniki_views.series_list, name='series-list'),
    path('genre/<int:genre_id>/', spravochniki_views.genre, name='genre'),
    path('genres/', spravochniki_views.genre_list, name='genre-list'),
    path('publishing_house/<int:publishing_house_id>/', spravochniki_views.publishing_house, name='publishing_house'),
    path('publishing_houses/', spravochniki_views.publishing_house_list, name='publishing_house-list'),
    path('', spravochniki_views.home)
]
