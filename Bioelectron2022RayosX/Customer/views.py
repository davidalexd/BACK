import json
from django.shortcuts import render
from django.http import JsonResponse

def api_customer(request, *args, **kwargs):
    body = request.body
    data = {}
    try: 
        data = json.loads(body)
    except:
        pass
    print(data.keys())
    return JsonResponse({"meesage":"Hola mundo"})