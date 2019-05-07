import json
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Book


def get_books_list(request):
    books_list = Book.objects.all()
    return render(request, 'books.html', {'books': books_list})


def retrieve(request, book_id):
    book = Book.objects.get(id=book_id)
    genres_queryset = book.genre.all()
    return render(request, 'book.html', {'book': book, 'genres': genres_queryset})


def create(request):
    data = json.loads(request.body)
    new_book = Book.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new book where id={new_book.id}.')

