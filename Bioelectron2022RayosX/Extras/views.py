from .apis_net_pe import TipoCambio
from .apis_regional_pe import Regional
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
            return JsonResponse({"data":{"Error":"Nro RUC debe de ser de tipo numérico"}}, safe=False)
    get_ruc_list_view = GET_RUC_ApiView

    def GET_DNI_ApiView(self,request):
        try:
            dni = int(request)
            queryset = TipoCambio(APIS_TOKEN).get_person(dni)
            return JsonResponse(queryset, safe=False)
        except:
            return JsonResponse({"error":"Nro DNI debe de ser de tipo numérico"}, safe=False)
    get_dni_list_view = GET_DNI_ApiView


class APIS_REGIONAL(StaffEditorPermissionMixin):
    def GET_DEPARTAMENTOS_ApiView(self):
        try:
            queryset = Regional().get_departamentos()
            return JsonResponse({"data":queryset}, safe=False) 
        except:
            return JsonResponse({"error":"No se encontraron departamentos"}, safe=False)

    get_dept_list_view = GET_DEPARTAMENTOS_ApiView

    def GET_DISTRITOS_ApiView(self,request):
        try:
            dept = str(request)
            queryset = Regional().get_distritos(dept)
            return JsonResponse({"data":queryset}, safe=False)
        except:
            return JsonResponse({"error":"No se encontraron Distritos"}, safe=False)
    get_dist_list_view = GET_DISTRITOS_ApiView

    def GET_PROVINCIAS_ApiView(self,request):
        try:
            dist = str(request)
            queryset = Regional().get_provincia(dist)
            return JsonResponse({"data":queryset}, safe=False)
        except:
            return JsonResponse({"error":"No se encontraron Provincias"}, safe=False)
    get_prov_list_view = GET_PROVINCIAS_ApiView