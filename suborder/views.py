import json
from django.http import HttpResponse
from .models import Suborder


def get_suborders_list(request):
    suborders_list = Suborder.objects.all()
    output = (' | ').join(str(i.id) for i in suborders_list)
    return HttpResponse(output)


def create(request):
    data = json.loads(request.body)
    new_suborder = Suborder.objects.create(**data)
    return HttpResponse(f'{request.method} method activated! Added new suborder where id={new_suborder.id}.')


def delete(request):
    data = json.loads(request.body)
    try:
        suborder = Suborder.objects.get(id=data['id'])
        suborder.delete()
        return HttpResponse(f'{request.method} method activated! Deleted suborder where id={data["id"]}.')
    except Suborder.DoesNotExist:
        return HttpResponse(f'Sorry, but suborder where id={data["id"]} does not exist')


def retrieve(request):
    data = json.loads(request.body)
    try:
        suborder = Suborder.objects.get(id=data['id'])
    except Suborder.DoesNotExist:
        return HttpResponse(f'Sorry, but suborder where id={data["id"]} does not exist')
    else:
        return HttpResponse(f'{request.method} method activated! You chose suborder #{suborder.id}:"{suborder.title}"')


def update(request):
    data = json.loads(request.body)
    try:
        suborder = Suborder.objects.get(id=data['id'])
        for key in data.keys():
            if key in suborder.__dict__.keys():
                suborder.__dict__[key] = data[key]
        suborder.save()
        return HttpResponse(f'{request.method} method activated! The suborder #{suborder.id} was updated"')
    except Suborder.DoesNotExist:
        return HttpResponse(f'Sorry, but suborder where id={data["id"]} does not exist')
