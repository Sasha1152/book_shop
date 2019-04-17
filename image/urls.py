from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_images_list, name='images_list'),
    path('create', views.create_image, name='create'),
    path('delete', views.delete_image, name='delete'),
    path('get', views.get_image, name='get'),
    path('update', views.update_image, name='update'),
]
