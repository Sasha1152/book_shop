from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_genres_list, name='genres_list'),
    path('create', views.create_genre, name='create'),
    path('delete', views.delete_genre, name='delete'),
    path('get', views.get_genre, name='get'),
    path('update', views.update_genre, name='update'),
]