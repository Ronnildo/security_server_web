from django.urls import path, include

# RestFramework
from rest_framework import routers

# Views
from .views import LoginView, HomeView, DetailsView,  DataViewSet, UserViewSet

router = routers.DefaultRouter()

router.register('files', DataViewSet)
# router.register('users', UserViewSet)

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/',HomeView.as_view(), name='home'),
    path('details/', DetailsView.as_view(), name='details'),
    path('routes/', include(router.urls), name='routers')
]

urlpatterns += router.urls