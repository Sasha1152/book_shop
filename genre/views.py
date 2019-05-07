import json
from django.http import HttpResponse
from .models import Genre



def get_genres_list(request):
    genres_list = Genre.objects.all()
    output = (' | ').join(i.name for i in genres_list)
    return HttpResponse(output)
