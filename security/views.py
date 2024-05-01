# HTTP
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages

# RestFramework
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

## Template
from django.views.generic import TemplateView

# Models e Form
from .models import Data, User
from .forms import UserForm
# Create your views here

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = User
    queryset = User.objects.all()

    def create(self, req, *args, **kwargs):
        serializer = self.serializer_class(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class DataViewSet(viewsets.ModelViewSet):
    serializer_class = Data
    queryset = Data.objects.all()

    def create(self, req, *args, **kwargs):
        serializer = self.serializer_class(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
class LoginView(TemplateView):
    template_name = 'index.html'

class HomeView(TemplateView):
    template_name = 'home/home.html'

class DetailsView(TemplateView):
    template_name = 'details/details.html'

# def login(req):
#     form = UserForm(req.POST or None)
#     if str(req.method) == 'POST':
#         if form.is_valid():
#             messages.success('Login efetuado!!')
#             form = UserForm()
#         else:
#             messages.error('E-mail ou senha Incorretos!!')
#     context = {
#         'form': form
#     }
#     return render(req, 'index.html', context)

def home(req):
    return render(req, 'home.html')
    # form = UserForm(req.POST or None)
    # # if str(req.user) != 'AnonymousUser':
    # if str(req.method) == 'POST':
    #     if form.is_valid():
    #         messages.success('Login efetuado!!')
    #         form = UserForm()
    #     else:
    #         messages.error('E-mail ou senha Incorretos!!')
    # context = {
    #     'form': form
    # }
    # else:
    #     return redirect('login')

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