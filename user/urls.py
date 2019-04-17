from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_users_list, name='users_list'),
    path('create', views.create_user, name='create'),
    path('delete', views.delete_user, name='delete'),
    path('get', views.get_user, name='get'),
    path('update', views.update_user, name='update'),
]
