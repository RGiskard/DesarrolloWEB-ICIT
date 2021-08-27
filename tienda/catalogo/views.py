from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def Home(request):
    return HttpResponse("Hello")
    #return "Hello World"

def Home2(request):
    return HttpResponse("Hello World 2")