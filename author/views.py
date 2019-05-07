import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author



def get_authors_list(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})


def retrieve(request, id):
    author = Author.objects.get(id=id)
    return render(request, 'author.html', {'author': author})


def create(request):
    data = json.loads(request.body)
    new_author = Author.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new author where id={new_author.id}.')
