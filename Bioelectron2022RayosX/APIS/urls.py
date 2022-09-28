from django.urls import path,include

urlpatterns = [
    path('',include('authentication.urls')),
    path('v1/',include('Customer.urls')),
    path('v1/',include('CompanyMachine.urls')),
    path('v2/',include('Customer.routers')),
    path('v2/',include('CompanyMachine.routers')),
]