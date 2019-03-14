from django.shortcuts import render


# Create your views here.
def index(request):
    """Домашняя страница приложения Learning Languages"""
    return render(request, 'learning_foreign_languages/index.html')
