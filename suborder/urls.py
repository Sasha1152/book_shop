from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_suborders_list, name='suborders_list'),
    path('create', views.create_suborder, name='create'),
    path('delete', views.delete_suborder, name='delete'),
    path('get', views.get_suborder, name='get'),
    path('update', views.update_suborder, name='update'),
]
