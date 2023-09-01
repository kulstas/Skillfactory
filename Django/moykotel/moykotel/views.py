from django.shortcuts import render


# Create your views here.
"""Функция отображения главной страницы"""
def index(request):
    return render(
        request,
        'index.html'
    )
