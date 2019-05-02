from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from book.models import Book


def add_book_to_the_cart(request):
    if request.GET.get('book_id'):
        try:
            list_books_id = request.session['books_in_my_cart']
            list_books_id.extend(request.GET.getlist('book_id'))
            request.session['books_in_my_cart'] = list_books_id
        except KeyError:
            request.session['books_in_my_cart'] = request.GET.getlist('book_id')
    return HttpResponseRedirect('/')


def delete_book_from_the_cart(request):
   pass


def show_cart(request):
    books = Book.objects.all()
    session_data = request.session.items()
    books_in_my_cart = request.session.get('books_in_my_cart')
    try:
        books = books.filter(id__in=books_in_my_cart)
    except TypeError:
        books = None

    return render(request, 'cart.html', {'session_data': session_data, 'books': books})
