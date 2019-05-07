from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_images_list, name='images_list'),
]
