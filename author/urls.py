from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_authors_list, name='authors_list'),
    path('<int:id>', views.get_author, name='author'),
    path('create', views.create_author, name='create'),
    path('delete', views.delete_author, name='delete'),
    path('get', views.get_author, name='get'),
    path('update', views.update_author, name='update'),
]
