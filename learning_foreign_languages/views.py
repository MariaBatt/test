from django.shortcuts import render
from .models import Language

# Create your views here.
def index(request):
    """Домашняя страница приложения Learning Languages"""
    return render(request, 'learning_foreign_languages/index.html')


def languages(request):
    """Выводит список языков"""
    languages = Language.objects.order_by('date_added')
    context = {'languages': languages}
    return render(request, 'learning_foreign_languages/languages.html', context)


def language(request, language_id):
    """Выводит один язык и все его записи"""
    language = Language.objects.get(id=language_id)
    vocabularies = language.vocabulary_set.order_by('-date_added')
    context = {'languages': languages, 'vocabularies': vocabularies}
    return render(request, 'learning_foreign_languages/languages.html', context)
