from django.http import HttpResponse
from .models import Image



def get_images_list(request):
    images_list = Image.objects.all()
    return HttpResponse(images_list)
