from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_books_list, name='books_list'),
    path('<int:id>', views.get_book, name='book'),
]
