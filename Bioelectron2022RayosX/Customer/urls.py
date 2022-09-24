from django.urls import path
from . import views

urlpatterns = [
    path('crear/',views.organzizaciones_create_view),
    path('<int:pk>/',views.organzizaciones_list_view)
]