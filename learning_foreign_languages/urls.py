"""Определяет схемы URL для maria_bs."""
from django.urls import path
from . import views

app_name = 'learning_foreign_languages'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
]