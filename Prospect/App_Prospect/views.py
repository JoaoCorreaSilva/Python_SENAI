from django.shortcuts import render
from .models import Cliente
from  django.contrib import  messages
# Create your views here.

def abre_index(request):
    return render(request, 'index.html')

def cad_cliente(request):
    return render(request, 'Cad_Cliente.html')

def salvar_cliente_novo(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        observacao = request.POST.get('observacao')
        grava_cliente = Cliente(
            nome=nome,
            telefone=telefone,
            email=email,
            observacao=observacao,
        )
        grava_cliente.save()
        messages.info(request, 'Cliente' + nome + ' cadastro com sucesso.')
        return render(request, 'Cad_Cliente.html')
