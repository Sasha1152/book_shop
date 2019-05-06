from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from book.models import Book


# TODO make each method more CRUDable
def add_books_to_the_cart(request):
    if request.GET.get('book_id'):
        try:
            set_books_id = set(request.session['books_in_my_cart'])
            set_books_id.update(set(request.GET.getlist('book_id')))
            list_books_id = list(set_books_id)
            request.session['books_in_my_cart'] = list_books_id
        except KeyError:
            book_set = set(request.GET.getlist('book_id'))
            request.session['books_in_my_cart'] = list(book_set)
    return HttpResponseRedirect('/')


# def add_one_book(request, book_id):
#     try:
#         set_books_id = set(request.session['books_in_my_cart'])
#         set_books_id.update(str(book_id))
#         list_books_id = list(set_books_id)
#         request.session['books_in_my_cart'] = list_books_id
#     except KeyError:
#         book_id = str(book_id)
#         request.session['books_in_my_cart'] = book_id
#     return HttpResponseRedirect('/')


def clear_cart(request):
    try:
        del request.session['books_in_my_cart']
        return HttpResponseRedirect('/cart')
    except KeyError:
        return HttpResponseRedirect('/cart')


def delete_book_from_the_cart(request, book_id):
    books_list = request.session['books_in_my_cart']
    books_list.remove(str(book_id))
    request.session['books_in_my_cart'] = books_list
    return HttpResponseRedirect('/cart')


def show_cart(request):
    books = Book.objects.all()
    session_data = request.session.items()
    books_in_my_cart = request.session.get('books_in_my_cart')
    try:
        books = books.filter(id__in=books_in_my_cart)
    except TypeError:
        books = None

    return render(request, 'cart.html', {'session_data': session_data, 'books': books})
