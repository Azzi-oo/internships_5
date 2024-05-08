from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('posts/', views.posts_list, name='posts_list'),
]
