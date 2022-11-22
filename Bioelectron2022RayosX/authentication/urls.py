from django.urls import path
from .views import Login, Logout,ProfileView
urlpatterns = [
    path('login/',Login.as_view(),name='Login'),
    path('user/',ProfileView.as_view(),name='User'),
    path('logout/', Logout.as_view(), name = 'logout'),
]