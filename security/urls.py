from django.urls import path
from . import views
from .views import LoginView, HomeView, DetailsView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/',HomeView.as_view(), name='home'),
    path('details/', DetailsView.as_view(), name='details'),
    # path('teste/', views.teste, name='teste')
]