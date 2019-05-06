from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Book


def get_books_list(request):
    books_list = Book.objects.all()
    return render(request, 'books.html', {'books': books_list})


def get_book(request, book_id):
    book = Book.objects.get(id=book_id)
    genres_queryset = book.genre.all()
    return render(request, 'book.html', {'book': book, 'genres': genres_queryset})


# TODO remove this
def add_one_book_to_the_cart(request, book_id):
    try:
        set_books_id = set(request.session['books_in_my_cart'])
        set_books_id.add(str(book_id))
        list_books_id = list(set_books_id)
        request.session['books_in_my_cart'] = list_books_id
        return HttpResponseRedirect('/book/' + str(book_id))
    except KeyError:
        request.session['books_in_my_cart'] = list(str(book_id))
    return HttpResponseRedirect('/book/' + str(book_id))
