from django.urls import path,include

urlpatterns = [
    path('Organizaciones/',include('Customer.urls'))
]