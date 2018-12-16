from rest_framework import serializers
from .models import Professor, Departamento, Curso, Disciplina, Turma, Avaliacao

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields =  ('pk', 'codigo', 'nome')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields =  ('pk', 'codigo', 'nome')


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields =  ('pk', 'departamento', 'codigo', 'nome')

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields =  ('pk', 'departamento','codigo', 'nome')

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields =  (
            'pk',
            'professor',
            'disciplina',
            'codigo', 
            'qnt_discentes',
            'tx_aprov',
            'media_turma',
            'qnt_tranc',
            'aprov_prim',
        )

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields =  ('pk', 'turma', 'codigo', 'auto_avaliacao','post_prof')