from django.shortcuts import render
from boards.models import Board


def home(request):
    return render(request, 'home.html', {'boards': Board.objects.all()})
