import json
from django.http import JsonResponse,HttpResponse
from django.forms.models import model_to_dict
from .models import OrganizacionModel

def api_customer(request, *args, **kwargs):
    model_data = OrganizacionModel.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(
            model_data,
            fields=["id","razon_social","ruc","nombre_comercial","tipo","ciiu","direccion_legal","pais_organizacion","departamento_organizacion","provincia_organizacion","distrito_organizacion","is_enabled"])
    return JsonResponse(data)
    #     data = dict(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str,headers={"content-type":"application/json"})