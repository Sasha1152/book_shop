from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_users_list, name='users_list'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
    path('retrieve', views.retrieve, name='retrieve'),
    path('update', views.update_user, name='update'),
]
