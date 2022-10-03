from .apis_net_pe import TipoCambio
from django.http import JsonResponse
from rest_framework import generics
from authentication.mixins import StaffEditorPermissionMixin

APIS_TOKEN = "apis-token-2946.7ev4pa8yPOAH1ylX2EkIwKNek9055ONj"

class APIS_EXTRAS(StaffEditorPermissionMixin):
    def GET_RUC_ApiView(self,request):
        try:
            ruc = int(request)
            queryset = TipoCambio(APIS_TOKEN).get_company(ruc)
            return JsonResponse(queryset, safe=False)
        except:
            return JsonResponse({"error":"Nro RUC debe de ser de tipo numérico"}, safe=False)

        

    get_ruc_list_view = GET_RUC_ApiView

    def GET_DNI_ApiView(self,request):
        try:
            dni = int(request)
            queryset = TipoCambio(APIS_TOKEN).get_person(dni)
            return JsonResponse(queryset, safe=False)
        except:
            return JsonResponse({"error":"Nro DNI debe de ser de tipo numérico"}, safe=False)

    get_dni_list_view = GET_DNI_ApiView

