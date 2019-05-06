from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_cart, name='cart'),
	path('add_books/', views.add_books_to_the_cart, name='add_books'),
	# path('add_book/<int:book_id>', views.add_one_book, name='add_book'),
	path('delete_book/<int:book_id>', views.delete_book_from_the_cart, name='delete_book'),
	path('clear_cart/', views.clear_cart, name='clear_cart'),
]