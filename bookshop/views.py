from django.shortcuts import render
from book.models import Book


def homepage(request):
    books_list = Book.objects.all()
    return render(request, 'home.html', {'books': books_list})
