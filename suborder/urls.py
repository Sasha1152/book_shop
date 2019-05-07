from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_suborders_list, name='suborders_list'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
    path('retrieve', views.retrieve, name='retrieve'),
    path('update', views.update, name='update'),
]
