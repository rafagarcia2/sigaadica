from rest_framework import serializers
from .models import Departamento


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('pk', 'codigo', 'nome', 'ativo', 'data_criacao')
