from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('teste/', views.teste, name='teste')
]