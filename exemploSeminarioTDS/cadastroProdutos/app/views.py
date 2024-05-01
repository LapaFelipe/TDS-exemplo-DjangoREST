from audioop import reverse

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework import viewsets
from rest_framework.views import APIView
from django.views import generic

from .forms import ProdutoForm
from app.models import Produto, Estoque
from app.serializers import ProdutoSerializer, EstoqueSerializer
from django.shortcuts import render
from .api import get_dados, create_dado, update_dado, delete_dado, get_dado

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

# class IndexView(generic.ListView):
#     model = Produto
#     template_name = "app/index.html"
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Produto.objects.order_by("nome")
#
# class ProdutoView(generic.ListView):
#     model = Produto
#     template_name = "app/listar_produto.html"
#
#     def get_queryset(self):
#         """Return the last five published questions."""
#         return Produto.objects.order_by("nome")
#
# class CadastrarProdutoView(generic.CreateView):
#     model = Produto
#     template_name = 'app/cadastrar_produto.html'
#     success_url = reverse_lazy('listar_produtos')
#
# class UpdateProdutoView(generic.UpdateView):
#     model = Produto
#     fields = ['nome', 'preco']
#     template_name = 'app/update_produtos.html'
#     success_url = reverse_lazy('listar_produtos')
#
# class DeleteProdutoView(generic.DeleteView):
#     model = Produto
#     template_name = 'app/delete_produtos.html'
#     success_url = reverse_lazy('listar_produtos')

def index(request):
    dados = get_dados()
    return render(request, 'app/listar_produto.html', {'dados': dados})

def create(request):
    if request.method == 'POST':
        novo_dado = {
            'nome': request.POST['nome'],
            'preco': request.POST['preco']
            # Adicione mais campos conforme necessário
        }
        create_dado(novo_dado)
        return redirect('listar_produtos')
    else:
        return render(request, 'app/cadastrar_produto.html')

def update(request, id):
    if request.method == 'POST':
        dados_atualizados = {
            'nome': request.POST['nome'],
            'preco': request.POST['preco']
        }
        update_dado(id, dados_atualizados)
        return redirect('listar_produtos')
    else:
        dado = get_dado(id)
        return render(request, 'app/update_produtos.html', {'dado': dado})

def delete(request, id):
    if request.method == "POST":
        delete_dado(id)
        return redirect('listar_produtos')
    else:
        dado = get_dado(id)
        return render(request, 'app/delete_produtos.html', {'dado': dado})