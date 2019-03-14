"""Определяет схемы URL для learning_foreign_languages."""
from django.urls import path
from . import views


urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]