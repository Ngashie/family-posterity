from cgitb import html
from html.entities import html5
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'base.html')

