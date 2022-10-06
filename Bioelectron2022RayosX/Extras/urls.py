from .apis_net_pe import ApisNetPe
from django.urls import path


APIS_TOKEN = "apis-token-2940.WZvoRT7R2m5SkjuMMpk0uNeKyFF6OrM7 "
api_consultas = ApisNetPe(APIS_TOKEN)

urlpatterns = [
    path('FILTERWITHRUC/',api_consultas.get_company("10460278975"),name='rucs-list'),
]