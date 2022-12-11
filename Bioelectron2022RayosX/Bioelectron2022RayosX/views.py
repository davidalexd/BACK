from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def error(request):
    context = {'segment': 'error'}
    html_template = loader.get_template('home/page-403.html')
    return HttpResponse(html_template.render(context, request))

def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/tables.html')
    return HttpResponse(html_template.render(context, request))

def report_create(request):
    context = {'segment': 'report_create'}
    html_template = loader.get_template('home/formato_reporte.html')
    return HttpResponse(html_template.render(context, request))

def login(request):
    context = {'segment': 'login'}
    html_template = loader.get_template('home/login.html')
    return HttpResponse(html_template.render(context, request))