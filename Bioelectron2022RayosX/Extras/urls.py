from django.urls import path,re_path
from . import views
urlpatterns = [
    path('FILTERWITHRUC/<request>',views.APIS_EXTRAS.get_ruc_list_view,name='rucs-list'),
    path('FILTERWITHDNI/<request>',views.APIS_EXTRAS.get_dni_list_view,name='dnis-list'),
    path('FILTERWITHDEPARTAMENTO/',views.APIS_REGIONAL.get_dept_list_view,name='dpts-list'),
    path('FILTERWITHDISTRITO/<request>',views.APIS_REGIONAL.get_dist_list_view,name='dpts-list'),
    path('FILTERWITHPROVINCIA/<request>',views.APIS_REGIONAL.get_prov_list_view,name='dpts-list'),
]

