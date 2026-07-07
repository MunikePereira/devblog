from rest_framework import serializers
from .models import Artigo,Categoria

class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo

        fields = ['id', 'titulo', 'conteudo', 'data_pubicacao']

class CategoriaSerializer(serializers.ModelSerializer):
    model = Categoria

    fields = ['id', 'nome']