from django.urls import path
from . import views


urlpatterns = [
    path('', views.retrieve, name='cart'),
	path('update/', views.update, name='update'),
	path('create#<int:book_id>', views.create, name='create'),
	path('delete_one/<int:book_id>', views.delete_one, name='delete_one'),
	path('delete_all/', views.delete_all, name='delete_all'),
]