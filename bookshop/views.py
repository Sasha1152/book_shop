from django.http import HttpResponseRedirect
from django.shortcuts import render
from book.models import Book
from datetime import datetime
from openpyxl import load_workbook
from author.models import Author
from genre.models import Genre


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


def import_books_from_xlsx(request):
    workbook = load_workbook('utils/booklist.xlsx')

    sheet = workbook['Sheet1']

    book = {}
    author = {}
    authors = Author.objects.all()
    for i in range(2, 10):
        book['title'] = sheet['b' + str(i)].value
        genre = sheet['c' + str(i)].value.lower()

        author_fullname = sheet['e' + str(i)].value
        if author_fullname:
            author_fullname = sheet['e' + str(i)].value.split(maxsplit=1)
            author['first_name'] = author_fullname[0]
            author['last_name'] = author_fullname[1]
        else:
            continue

        price = sheet['h' + str(i)].value
        if price[0] == '$':
            book['price'] = sheet['h' + str(i)].value[1:]
        else:
            book['price'] = price

        if author['first_name'] not in authors.filter(first_name='first_name') and author['last_name'] not in authors.filter(last_name='last_name'):
            Author.objects.create(first_name=author['first_name'], last_name=author['last_name'])

    return HttpResponseRedirect('/')