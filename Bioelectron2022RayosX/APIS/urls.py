from django.urls import path,include

urlpatterns = [
    path('',include('authentication.urls')),
    path('v1/',include('Customer.urls')),
    path('v1/',include('CompanyMachine.urls')),
    path('v1/',include('Machine.urls')),
    path('v1/',include('Operations.urls')),
    path('v1/',include('Protocol.urls')),
    path('v2/Customer/',include('Customer.routers')),
    path('v2/CompanyMachine/',include('CompanyMachine.routers')),
    path('v2/Machine/',include('Machine.routers')),
    path('v2/Operation/',include('Operations.routers')),
    path('v2/Protocol/',include('Protocol.routers')),
]