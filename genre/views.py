import json
from django.http import HttpResponse
from .models import Genre



def get_genres_list(request):
    genres_list = Genre.objects.all()
    output = (' | ').join(i.name for i in genres_list)
    return HttpResponse(output)


def create_genre(request):
    data = json.loads(request.body)
    new_genre = Genre.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new genre where id={new_genre.id}.')


def delete_genre(request):
    data = json.loads(request.body)
    try:
        genre = Genre.objects.get(id=data['id'])
        genre.delete()
        return HttpResponse(f'{request.method} method activated! Deleted genre where id={data["id"]}.')
    except Genre.DoesNotExist:
        return HttpResponse(f'Sorry, but genre where id={data["id"]} does not exist')


def get_genre(request):
    data = json.loads(request.body)
    try:
        genre = Genre.objects.get(id=data['id'])
    except Genre.DoesNotExist:
        return HttpResponse(f'Sorry, but genre where id={data["id"]} does not exist')
    else:
        return HttpResponse(f'{request.method} method activated! You chose genre #{genre.id}:"{genre.title}"')


def update_genre(request):
    data = json.loads(request.body)
    try:
        genre = Genre.objects.get(id=data['id'])
        for key in data.keys():
            if key in genre.__dict__.keys():
                genre.__dict__[key] = data[key]
        genre.save()
        return HttpResponse(f'{request.method} method activated! The genre #{genre.id} was updated"')
    except Genre.DoesNotExist:
        return HttpResponse(f'Sorry, but genre where id={data["id"]} does not exist')
