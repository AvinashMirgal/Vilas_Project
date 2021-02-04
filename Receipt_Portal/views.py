from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'index.html', context)

def demo(request):
    context = {}
    return render(request, 'demo.html', context)

def table(request):
    context = {}
    return render(request, 'table.html', context)