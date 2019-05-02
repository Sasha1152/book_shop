from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_cart, name='cart'),
	path('add_book/', views.add_book_to_the_cart, name='add_book'),
	path('delete_book/', views.delete_book_from_the_cart, name='delete_book'),
]