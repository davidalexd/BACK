from django.urls import path,include

urlpatterns = [
    path('api/',include('authentication.urls')),
    path('api/v1/',include('Customer.urls')),
    path('api/v2/',include('Customer.routers'))
]