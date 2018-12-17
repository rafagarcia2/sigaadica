from rest_framework import serializers
from .models import Departamento, Curso, Disciplina


class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('pk', 'codigo', 'nome', 'ativo', 'data_criacao')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('pk', 'codigo', 'nome', 'ativo', 'data_criacao')


class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ('pk', 'id_componente', 'nome', 'departamento', 'ativo', 'data_criacao')
