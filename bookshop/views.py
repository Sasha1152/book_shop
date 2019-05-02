from django.shortcuts import render
from book.models import Book
from django.http import HttpResponse


# def homepage(request):
#     books = Book.objects.all()
#     print(books.query)
#     authors = Author.objects.all()
#     genres = Genre.objects.all()
#     user = User.objects.get(id=1)
#     if request.GET:
#         if request.GET.get('author_id'):
#             author_id = dict(request.GET).get('author_id')
#             books = books.filter(author__id__in=author_id)
#         if request.GET.get('genre_id'):
#             genre_id = dict(request.GET).get('genre_id')
#             books = books.filter(genre__id__in=genre_id)
#     return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres, 'user': user})


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
        if request.GET.get('book_id'):
            try:
                list_books_id = request.session['books_in_my_cart']
                list_books_id.extend(request.GET.getlist('book_id'))
                request.session['books_in_my_cart'] = list_books_id
            except KeyError:
                request.session['books_in_my_cart'] = request.GET.getlist('book_id')

    # print('MYPRINT end function homepage: ', request.session['books_in_my_cart'])
    return render(request, 'home.html', {'books': books, 'authors': authors, 'genres': genres})


def show_cart(request):
    books = Book.objects.all()
    session_data = request.session.items()
    books_in_my_cart = request.session.get('books_in_my_cart')
    # print('MYPRINT books_in_my_cart: ', books_in_my_cart)
    try:
        books = books.filter(id__in=books_in_my_cart)
    except TypeError:
        books = None

    return render(request, 'cart.html', {'session_data': session_data, 'books': books})
