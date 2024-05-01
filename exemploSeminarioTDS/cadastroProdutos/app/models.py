from audioop import reverse

from django.db import models
from django.shortcuts import redirect


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField(default=1.99)
    data_cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def get_success_url(self):
        return redirect("listar_produtos")

class Estoque(models.Model):
    produto_pk = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)

    def get_success_url(self):
        return redirect("listar_produtos")


