from django.shortcuts import render
from book.models import Book
from author.models import Author
from genre.models import Genre


def homepage(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    print("MYPRINT: ", genres)
    return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres})
