from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from django.shortcuts import get_object_or_404

from .serializers import ProfessorSerializer
from .serializers import DepartamentoSerializer
from .serializers import CursoSerializer
from .serializers import DisciplinaSerializer
from .serializers import TurmaSerializer
from .serializers import AvaliacaoSerializer
from .models import Professor, Departamento, Curso, Disciplina, Turma, Avaliacao

'''
class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Departamentos.
    """
    queryset = Departamento.objects.all().order_by('-nome')
    serializer_class = DepartamentoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita disciplinas
    """
    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all()
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'id_componente'
    search_fields = ('nome',)
'''
class ProfessorViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Professor.
    """
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all() 

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Departamento.
    """
    serializer_class = DepartamentoSerializer
    queryset = Departamento.objects.all() 

class CursoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Curso.
    """
    serializer_class = CursoSerializer
    queryset = Curso.objects.all() 
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Disciplina.
    """
    serializer_class = DisciplinaSerializer
    queryset = Disciplina.objects.all() 

class TurmaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Turma.
    """
    serializer_class = TurmaSerializer
    queryset = Turma.objects.all() 

class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Avaliacao.
    """
    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()

### CURSOS ###

@api_view(['GET'])
def curso(request):
    """
    Exibe todos os cursos
    """
    cursos_serializer = CursoSerializer(Curso.objects.all(), many=True)

    return Response(cursos_serializer.data)


@api_view(['GET'])
def curso_id(request, id):
    """
    Devolve um curso específico
    """
    curso = get_object_or_404(Curso, pk=id)
    curso_serializer = CursoSerializer(curso)

    return Response(curso_serializer.data)


@api_view(['GET'])
def curso_por_departamento(request, id):
    """
    Recupera todos os cursos de um determinado departamento
    """
    pass



### DISCIPLINA ###


@api_view(['GET'])
def disciplinas(request):
    """
    Recupera todas as disciplinas cadastradas
    """
    disciplinas = Disciplina.objects.all()
    disciplinas_serialized = DisciplinaSerializer(disciplinas, many=True)

    return Response(disciplinas_serialized.data)


@api_view(['GET'])
def disciplina_id(request, id):
    """
    Recupera uma disciplina específica pelo seu id
    """
    disciplina = get_object_or_404(Disciplina, pk=id)
    disciplina_serialized = DisciplinaSerializer(disciplina)

    return Response(disciplina_serialized.data)


@api_view(['GET'])
def pesquisa_disciplina(request):
    """
    Recupera uma disciplina de acordo com seu nome ou código
    """
    pesquisa = request.GET.get('nome')

    disciplina = get_object_or_404(Disciplina, Q(nome__icontains=pesquisa) | Q(codigo=pesquisa))
    disciplina_serialized = DisciplinaSerializer(disciplina)

    return Response(disciplina_serialized.data)