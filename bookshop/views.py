from django.shortcuts import render
from book.models import Book
from datetime import datetime


# def homepage(request):
#     books = Book.objects.all()
#     authors = []
#     genres = []
#     # TODO make one query to avoid n+1 issue https://stackoverflow.com/questions/13092268/how-do-you-join-two-tables-on-a-foreign-key-field-using-django-orm
#     for book in books:
#         if book.author not in authors:
#             authors.append(book.author)
#         for genre in book.genre.all():
#             if genre not in genres:
#                 genres.append(genre)
#     if request.GET:
#         if request.GET.get('author_id'):
#             author_id = request.GET.getlist('author_id')
#             books = books.filter(author__id__in=author_id)
#         if request.GET.get('genre_id'):
#             genre_id = request.GET.getlist('genre_id')
#             books = books.filter(genre__id__in=genre_id)
#     return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres})


def homepage(request):
    start_time = datetime.now()

    books = Book.objects.prefetch_related('author', 'genre').all()
    # books = Book.objects.all()
    # print('MYPRINT: ', books.author.first_name)
    authors = []
    genres = []
    for book in books:
        if book.author not in authors:
            authors.append(book.author)
        for genre in book.genre.all():
            if genre not in genres:
                genres.append(genre)
    if request.GET:
        if request.GET.get('author_id'):
            author_id = request.GET.getlist('author_id')
            books = books.filter(author__id__in=author_id)
        if request.GET.get('genre_id'):
            genre_id = request.GET.getlist('genre_id')
            books = books.filter(genre__id__in=genre_id)
    end_time = datetime.now()
    print('Duration: {}'.format(end_time - start_time))
    return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres})
