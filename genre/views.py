import json
from django.http import HttpResponse
from .models import Genre



def get_genres_list(request):
    genres_list = Genre.objects.all()
    output = (' | ').join(i.name for i in genres_list)
    return HttpResponse(output)


def create(request):
    data = json.loads(request.body)
    new_genre = Genre.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new genre where id={new_genre.id}.')
