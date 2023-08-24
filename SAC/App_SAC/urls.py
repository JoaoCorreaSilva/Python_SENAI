from django.urls import path
from . import views

urlpatterns = [
    path('', views.abre_index, name='abre-index'),
    path('cad_cliente', views.cad_cliente, name='cad-cliente'),
    path('salvar_cliente_novo', views.salvar_cliente_novo, name='salvar_cliente_novo'),
    path('cons_cliente', views.cons_cliente, name='cons_cliente'),
    path('edit_cliente/<int:id>', views.edit_cliente, name='cons_cliente'),
    path('salvar_cliente_editado', views.salvar_cliente_editado, name='salvar_cliente_editado'),
    path('excluir_cliente/<int:id>', views.delete_cliente, name='excluir_cliente'),
]
