from django.shortcuts import render
from django.http import Http404

from .models import User
# Create your views here


def login(req):
    users = User.objects.all()
    return render(req, 'index.html', {"users": users})

def home(req):
    # try:
    #     user = User.objects.get(pk=user_id)
    # except Http404:
    #     return Http404('Error')
    return render(req, "home.html")

def details(req):
    return render(req, "details.html")