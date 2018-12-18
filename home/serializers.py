from rest_framework import serializers
from .models import Departamento, Curso, Disciplina


from rest_framework import serializers
from .models import Professor, Departamento, Curso, Disciplina, Turma, Avaliacao

class ProfessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Professor
        fields =  (
            'pk',
            'codigo',
            'nome',
            'vinculo'
        )

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields =  (
            'pk',
            'codigo',
            'nome'
        )


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields =  (
            'pk',
            'departamento',
            'codigo',
            'nome'
        )

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields =  (
            'pk',
            'id_componente',
            'departamento',
            'codigo',
            'nome'
        )

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields =  (
            'pk',
            'professor',
            'disciplina',
            'codigo',
            'anoperiodo',
            'qnt_discentes',
            'qnt_aprovados',
            'qnt_reprovados',
            'qnt_trancamentos',
            'qnt_aprovados_primeira',
            'qnt_reposicao',
            'taxa_aprovacao',
            'taxa_reprovacao',
            'evasao',
            'media_turma',
            'media_faltas',
        )

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields =  (
            'pk', 
            'turma', 
            'codigo', 
            'postura_profissional_media',
            'postura_profissional_dp',
            'atuacao_profissional_media',
            'atuacao_profissional_dp',
            'autoavaliacao_aluno_media',
            'autoavaliacao_aluno_dp',
        )