from django.shortcuts import render


def index(request):
    """Главная страница"""
    template = 'main/index.html'
    return render(request, template)


def post(request):
    template = 'main/index.html'
    return render(request, template)
