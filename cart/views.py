from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from book.models import Book


def update(request):
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


def create(request, book_id):
    try:
        set_books_id = set(request.session['books_in_my_cart'])
        set_books_id.add(str(book_id))
        list_books_id = list(set_books_id)
        request.session['books_in_my_cart'] = list_books_id
        return HttpResponseRedirect('/book/' + str(book_id))
    except KeyError:
        request.session['books_in_my_cart'] = list(str(book_id))
    return HttpResponseRedirect('/book/' + str(book_id))


def delete_all(request):
    try:
        del request.session['books_in_my_cart']
        return HttpResponseRedirect('/cart')
    except KeyError:
        return HttpResponseRedirect('/cart')


def delete_one(request, book_id):
    books_list = request.session['books_in_my_cart']
    books_list.remove(str(book_id))
    request.session['books_in_my_cart'] = books_list
    return HttpResponseRedirect('/cart')


def retrieve(request):
    books = Book.objects.all()
    session_data = request.session.items()
    books_in_my_cart = request.session.get('books_in_my_cart')
    try:
        books = books.filter(id__in=books_in_my_cart)
    except TypeError:
        books = None

    return render(request, 'cart.html', {'session_data': session_data, 'books': books})
