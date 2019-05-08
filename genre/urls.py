from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_genres_list, name='genres_list'),
    path('', views.create, name='create'),
]
