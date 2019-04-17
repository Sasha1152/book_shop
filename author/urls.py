from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_authors_list, name='authors_list'),
    path('create', views.create_author, name='create'),
    path('delete', views.delete_author, name='delete'),
    path('get', views.get_author, name='get'),
    path('update', views.update_author, name='update'),
]
