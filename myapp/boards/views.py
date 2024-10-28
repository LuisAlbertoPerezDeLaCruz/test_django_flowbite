from django.shortcuts import render, HttpResponse
from boards.models import Board


def home(request):
    return render(request, 'home.html', {'boards': Board.objects.all()})


def board_topics(request, id):
    board = Board.objects.get(id=id)
    return render(request, 'topics.html', {'board': board})
