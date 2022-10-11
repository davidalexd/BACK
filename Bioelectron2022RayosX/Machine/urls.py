from django.urls import path
from . import views

urlpatterns = [
    path('Sistemas/',views.sistemas_create_view,name='sistema-list'),
    path('Sistemas/<int:pk>/',views.sistemas_list_view,name='sistema-detail'),
    path('Sistemas/<int:pk>/update/',views.sistemas_actualizar_view,name='sistema-update'),
    path('Sistemas/<int:pk>/delete/',views.sistemas_eliminar_view,name='sistema-delete'),

    path('Tubos/',views.tubos_create_view,name='tubo-list'),
    path('Tubos/<int:pk>/',views.tubos_list_view,name='tubo-detail'),
    path('Tubos/<int:pk>/update/',views.tubos_actualizar_view,name='tubo-update'),
    path('Tubos/<int:pk>/delete/',views.tubos_eliminar_view,name='tubo-delete'),
    
    # path('SistemasHistory/',views.sistema_history_view,name='sistema-history-list'),
    # path('TubosHistory/',views.tubo_history_view,name='tubo-history-list'),
]