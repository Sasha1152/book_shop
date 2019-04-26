from django.shortcuts import render
from book.models import Book
from author.models import Author
from genre.models import Genre
from user.models import User


def homepage(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    user = User.objects.get(id=1)
    if request.GET:
        if request.GET.get('author_id'):
            author_id = dict(request.GET).get('author_id')
            books = books.filter(author__id__in=author_id)
        if request.GET.get('genre_id'):
            genre_id = dict(request.GET).get('genre_id')
            books = books.filter(genre__id__in=genre_id)
    return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres, 'user': user})
