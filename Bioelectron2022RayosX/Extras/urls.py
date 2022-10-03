from django.urls import path,re_path
from . import views
urlpatterns = [
    path('FILTERWITHRUC/<request>',views.APIS_EXTRAS.get_ruc_list_view,name='rucs-list'),
    path('FILTERWITHDNI/<request>',views.APIS_EXTRAS.get_dni_list_view,name='dnis-list'),
]