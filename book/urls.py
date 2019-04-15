from django.conf.urls import url
from django.urls import path

from . import views
urlpatterns = [
    url(r'^$', views.get_book_list, name='book_list'),
    path('create', views.create_book, name='create'),
    path('delete', views.delete_book, name='delete'),
    path('show', views.show_book, name='show'),
    path('update', views.update_book, name='update'),
]
