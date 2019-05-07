from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_orders_list, name='orders_list'),
    path('<int:id>', views.retrieve, name='retrieve'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]
