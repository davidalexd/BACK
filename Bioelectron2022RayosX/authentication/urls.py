from django.urls import path
from .views import Login, Logout
urlpatterns = [
    path('Login/',Login.as_view(),name='Login'),
    path('Logout/',Logout.as_view(),name='Login')
]