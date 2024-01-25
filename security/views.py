from django.shortcuts import render
from django.http import Http404
from django.contrib import messages

from .models import User
from .forms import UserForm
# Create your views here

def login(req):
    form = UserForm(req.POST or None)

    if str(req.method) == 'POST':
        if form.is_valid():
            messages.success('Login efetuado!!')
            form = UserForm()
        else:
            messages.error('E-mail ou senha Incorretos!!')
    context = {
        'form': form
    }
    return render(req, 'index.html', context)

def home(req):
    return render(req, "home.html")

def details(req):
    return render(req, "details.html")

def teste(req):
    form = UserForm(req.POST or None)

    if str(req.method) == 'POST':
        if form.is_valid():
            messages.success('Login efetuado!!')
            form = UserForm()
        else:
            messages.error('E-mail ou senha Incorretos!!')
    context = {
        'form': form
    }
    return render(req, 'teste.html', context)