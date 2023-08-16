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

#query set Tipos de Look Up

# nome__exact='SS' - tem que ser exatamente igual
# nome__contains='H' - contem o H maiusculo
# nome__icontains='H' - ignora se maiúsculo ou minúsculo
# nome__startswith='M' - traz o que começa com a letra M ou sequencia de letras
# nome__istartswith='M' - traz o que começa com a letra M ignorando se maiusculo ou minusculo u sequencia de letras
# nome__endswith='a' - traz o que termina com a letra a minusculo ou sequencia de letras
# nome__iendswith='a' - traz o que termina com a letra a ignorando maiúsculo ou minusculo
# nome__in=['Michael', 'Obama']) traz somente os nome que estão na lista
# Pode ser feito uma composição 'and' utilizando , (virgula entre os campos) ou 'or' utilizando | (pipe entre os campos)

def cons_cliente(request):
    dado_pesquisa_nome = request.POST.get('cliente')
    dado_pesquisa_telefone = request.POST.get('telefone')
    dado_pesquisa_email = request.POST.get('email')

    if dado_pesquisa_nome != None and dado_pesquisa_nome != '':
        clientes = Cliente.objects.filter(nome__icontains=dado_pesquisa_nome)
        return render(request, 'Cons_Cliente_Lista.html',{'dados_clientes': clientes})

    elif dado_pesquisa_telefone != None and dado_pesquisa_telefone != '':
        clientes = Cliente.objects.filter(nome__icontains=dado_pesquisa_telefone)
        return render(request, 'Const_Cliente_Lista.html', {'dados_clientes' : clientes})

    elif dado_pesquisa_email != None and dado_pesquisa_email != '':
        clientes = Cliente.objects.filter(nome__icontains=dado_pesquisa_email)
        return render(request, 'Const_Cliente_Lista.html', {'dados_clientes' : clientes})
