from django.shortcuts import render
from book.models import Book
from author.models import Author
from genre.models import Genre


def homepage(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    if request.GET.get('author_id'):
        author_id = request.GET.get('author_id')
        books = books.filter(author__id=author_id)
    if request.GET.get('genre_id'):
        genre_id = request.GET.get('genre_id')
        books = books.filter(genre__id=genre_id)
    return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres})
