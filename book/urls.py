from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_books_list, name='books_list'),
    path('create', views.create_book, name='create'),
    path('delete', views.delete_book, name='delete'),
    path('get', views.get_book, name='get'),
    path('update', views.update_book, name='update'),
]
