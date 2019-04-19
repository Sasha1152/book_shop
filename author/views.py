import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Author



def get_authors_list(request):
    authors_list = Author.objects.all()
    return render(request, 'authors.html', {'authors': authors_list})


def get_author(request, id):
    author = Author.objects.get(id=id)
    return HttpResponse(author)


def create_author(request):
    data = json.loads(request.body)
    new_author = Author.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new author where id={new_author.id}.')


def delete_author(request):
    data = json.loads(request.body)
    try:
        author = Author.objects.get(id=data['id'])
        author.delete()
        return HttpResponse(f'{request.method} method activated! Deleted author where id={data["id"]}.')
    except Author.DoesNotExist:
        return HttpResponse(f'Sorry, but author where id={data["id"]} does not exist')


def update_author(request):
    data = json.loads(request.body)
    try:
        author = Author.objects.get(id=data['id'])
        for key in data.keys():
            if key in author.__dict__.keys():
                author.__dict__[key] = data[key]
        author.save()
        return HttpResponse(f'{request.method} method activated! The author #{author.id} was updated"')
    except Author.DoesNotExist:
        return HttpResponse(f'Sorry, but author where id={data["id"]} does not exist')
