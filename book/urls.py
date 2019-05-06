from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_books_list, name='books_list'),
    path('<int:book_id>', views.get_book, name='book'),
    path('<int:book_id>add_book', views.add_one_book_to_the_cart, name='add_book'),
]
