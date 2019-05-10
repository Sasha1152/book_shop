from django.http import HttpResponseRedirect
from django.shortcuts import render
from book.models import Book
from datetime import datetime
from openpyxl import load_workbook
from author.models import Author
from genre.models import Genre


def homepage(request):
    start_time = datetime.now()

    books = Book.objects.prefetch_related('author', 'genre').all()
    # books = Book.objects.all()
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

    books_in_database = list(Book.objects.all())
    books_in_database = [book.title for book in books_in_database]
    new_books = []

    genres_in_database = Genre.objects.all()
    genres_in_database = [genre.name for genre in genres_in_database]
    new_genres = []

    authors_in_database = Author.objects.all()
    authors_in_database_list = [(author.first_name + ' ' + author.last_name) for author in list(authors_in_database)]
    new_authors = []

    for i in range(2, 1000):
        author_fullname = sheet['e' + str(i)].value
        book_title = sheet['b' + str(i)].value
        if not book_title or not author_fullname:
            continue

        author_first_name = author_fullname.split(maxsplit=1)[0]
        try:
            author_last_name = author_fullname.split(maxsplit=1)[1]
        except IndexError:
            author_last_name = None

        if author_fullname not in new_authors and author_fullname not in authors_in_database_list:
            Author.objects.create(first_name=author_first_name, last_name=author_last_name)
            new_authors.append(author_fullname)

        price = sheet['h' + str(i)].value
        if price[0] == '$':
            price = sheet['h' + str(i)].value[1:]

        genre = sheet['c' + str(i)].value.lower()
        if genre not in genres_in_database and genre not in new_genres:
            new_genre = Genre.objects.create(name=genre)
            new_genres.append(genre)
        else:
            new_genre = Genre.objects.get(name=genre)

        if book_title not in books_in_database and book_title not in new_books:
            new_book = Book.objects.create(
                title=book_title,
                price=price,
                author_id=Author.objects.get(first_name=author_first_name, last_name=author_last_name).id,
            )
            new_book.genre.add(new_genre)

    return HttpResponseRedirect('/')
