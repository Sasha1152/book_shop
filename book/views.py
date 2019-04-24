from django.shortcuts import render
from .models import Book


def get_books_list(request):
    books_list = Book.objects.all()
    return render(request, 'books.html', {'books': books_list})


def get_book(request, id):
    book = Book.objects.get(id=id)
    genres_queryset = book.genre.all()
    return render(request, 'book.html', {'book': book, 'genres': genres_queryset})
