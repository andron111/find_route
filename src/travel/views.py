from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    name = 'Andrei'
    return render(request, 'home.html', {'name': name})


def about(request):
    name = 'Nadia'
    return render(request, 'about.html', {'name': name})


