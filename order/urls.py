from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_orders_list, name='orders_list'),
    path('<int:id>', views.get_order, name='order'),
    path('create', views.create_order, name='create'),
    path('delete', views.delete_order, name='delete'),
    path('get', views.get_order, name='get'),
    path('update', views.update_order, name='update'),
]
