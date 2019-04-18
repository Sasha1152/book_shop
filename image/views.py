import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Image



def get_images_list(request):
    images_list = Image.objects.all()
    return HttpResponse(images_list)


def create_image(request):
    data = json.loads(request.body)
    new_image = Image.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new image where id={new_image.id}.')


def delete_image(request):
    data = json.loads(request.body)
    try:
        image = Image.objects.get(id=data['id'])
        image.delete()
        return HttpResponse(f'{request.method} method activated! Deleted image where id={data["id"]}.')
    except Image.DoesNotExist:
        return HttpResponse(f'Sorry, but image where id={data["id"]} does not exist')


def get_image(request):
    data = json.loads(request.body)
    try:
        image = Image.objects.get(id=data['id'])
    except Image.DoesNotExist:
        return HttpResponse(f'Sorry, but image where id={data["id"]} does not exist')
    else:
        return HttpResponse(f'{request.method} method activated! You chose image #{image.id}:"{image.title}"')


def update_image(request):
    data = json.loads(request.body)
    try:
        image = Image.objects.get(id=data['id'])
        for key in data.keys():
            if key in image.__dict__.keys():
                image.__dict__[key] = data[key]
        image.save()
        return HttpResponse(f'{request.method} method activated! The image #{image.id} was updated"')
    except Image.DoesNotExist:
        return HttpResponse(f'Sorry, but image where id={data["id"]} does not exist')
