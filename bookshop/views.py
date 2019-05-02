from django.shortcuts import render
from book.models import Book


def homepage(request):
    books = Book.objects.all()
    authors = []
    genres = []
    for book in books:
        if book.author not in authors:
            authors.append(book.author)
        for genre in book.genre.all():
            if genre not in genres:
                genres.append(genre)
    # request.session.clear()
    if request.GET:
        if request.GET.get('author_id'):
            author_id = request.GET.getlist('author_id')
            books = books.filter(author__id__in=author_id)
        if request.GET.get('genre_id'):
            genre_id = request.GET.getlist('genre_id')
            books = books.filter(genre__id__in=genre_id)
    return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres})
