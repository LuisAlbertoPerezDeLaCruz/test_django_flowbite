from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'boards_main.html', {'saludo': 'Hello World !!!'})
