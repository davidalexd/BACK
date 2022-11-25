from django.urls import path
from .views import Login, Logout,ProfileView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/',Login.as_view(),name='Login'),
    path('user/',ProfileView.as_view(),name='User'),
    path('logout/', Logout.as_view(), name='Logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]