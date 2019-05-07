from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_authors_list, name='authors_list'),
    path('<int:id>', views.retrieve, name='author'),
    path('create', views.create, name='create'),
]
