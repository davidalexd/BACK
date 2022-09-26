from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['POST'])
def api_home(request, *args, **kwargs):
    return Response()