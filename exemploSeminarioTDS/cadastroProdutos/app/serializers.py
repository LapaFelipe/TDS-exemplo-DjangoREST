from app.models import Produto, Estoque
from rest_framework import serializers

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            "id", "nome", "preco", "data_cadastro"
        ]

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = [
            "id", "produto_pk", "quantidade"
        ]



