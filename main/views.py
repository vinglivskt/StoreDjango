from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {'title': 'Главная страница',
               'text': 'Это главная страница'}
    return render(request, 'main/index.html', context)
