from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.get_books_list, name='books_list'),
    re_path(r'<id>', views.get_book, name='book'),
    path('create', views.create_book, name='create'),
    path('delete', views.delete_book, name='delete'),
    path('get', views.get_book, name='get'),
    path('update', views.update_book, name='update'),
]
