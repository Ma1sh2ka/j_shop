from django.urls import path

from books import views as books_views
app_name = 'books'

urlpatterns = [
    path('book/<int:pk>/', books_views.BookDetailView.as_view(), name='book'),
    path('books', books_views.BookListView.as_view(), name='book-list'),
    path('create-book/', books_views.BookCreateView.as_view(), name='book_create'),
    path('update-book/<int:pk>/', books_views.BookUpdateView.as_view(), name='book_update'),
    path('delete-book/<int:pk>/', books_views.BookDeleteView.as_view(), name='book_delete')
]