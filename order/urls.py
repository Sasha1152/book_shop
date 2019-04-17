from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.get_orders_list, name='orders_list'),
    path('create', views.create_order, name='create'),
    path('delete', views.delete_order, name='delete'),
    path('get', views.get_order, name='get'),
    path('update', views.update_order, name='update'),
]
