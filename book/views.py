from django.shortcuts import render
import json
from django.http import HttpResponse
from .models import Book


def get_book_list(request):
    book_list = Book.objects.all()
    # output = (', ').join([i.title for i in book_list])
    return HttpResponse(book_list[0].title)


def create_book(request):
    data = json.loads(request.body)
    new_book = Book.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new book where id={new_book.id}.')


def delete_book(request):
    data = json.loads(request.body)
    try:
        book = Book.objects.get(id=data['id'])
        book.delete()
        return HttpResponse(f'{request.method} method activated! Deleted book where id={data["id"]}.')
    except Book.DoesNotExist:
        return HttpResponse(f'Sorry, but book where id={data["id"]} does not exist')


def show_book(request):
    data = json.loads(request.body)
    try:
        book = Book.objects.get(id=data['id'])
    except Book.DoesNotExist:
        return HttpResponse(f'Sorry, but book where id={data["id"]} does not exist')
    else:
        return HttpResponse(f'{request.method} method activated! You chose book #{book.id}:"{book.title}"')


def update_book(request):
    data = json.loads(request.body)
    try:
        book = Book.objects.get(id=data['id'])
        for key in data.keys():
            if key in book.__dict__.keys():
                book.__dict__[key] = data[key]
        book.save()
        return HttpResponse(f'{request.method} method activated! The book #{book.id} was updated"')
    except Book.DoesNotExist:
        return HttpResponse(f'Sorry, but book where id={data["id"]} does not exist')
