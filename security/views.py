from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def login(req):
    return render(req, 'index.html')

def home(req):
    return render(req, "home.html")

def details(req):
    return render(req, "details.html")