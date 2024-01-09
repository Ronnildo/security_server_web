from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def login(req):
    return HttpResponse("Página de Login")

def home(req):
    return HttpResponse("Página Home")

def details(req):
    return HttpResponse("Página de Detalhes")