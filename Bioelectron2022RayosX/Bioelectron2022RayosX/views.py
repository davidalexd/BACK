from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/tables.html')
    return HttpResponse(html_template.render(context, request))

