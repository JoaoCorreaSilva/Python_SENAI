from django.urls import path
from . import views

urlpatterns = [
    path('', views.abre_index, name='abre-index'),
    path('cad_cliente', views.cad_cliente, name='cad-cliente'),
    path('salvar_cliente_novo', views.salvar_cliente_novo, name='salvar_cliente_novo'),
    path('const_cliente', views.cons_cliente, name='cons_cliente'),
]
