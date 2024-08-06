from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html')

def about(request):
    return render(request, 'recipes/about.html')

def contats(request):
    return HttpResponse('<h1>Contats</h1>')

