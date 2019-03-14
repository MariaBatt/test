"""Определяет схемы URL для learning_foreign_languages."""
from django.urls import path
from . import views

app_name = 'learning_foreign_languages'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    #Вывод всех языков.
    path('languages/', views.languages, name='languages'),
    # Страница с подробной информацией по языку
    path('languages/<int:language_id>/', views.language, name='language')
]