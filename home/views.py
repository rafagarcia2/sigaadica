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

class ProfessorViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Professor.
    """
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'pk'
    search_fields = ('nome',)


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Departamento.
    """
    queryset = Departamento.objects.all() 
    serializer_class = DepartamentoSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'pk'
    search_fields = ('nome',)

class CursoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Curso.
    """
    queryset = Curso.objects.all() 
    serializer_class = CursoSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'pk'
    search_fields = ('nome',)
    
class DisciplinaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Disciplina.
    """
    queryset = Disciplina.objects.all() 
    serializer_class = DisciplinaSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'pk'
    search_fields = ('nome',)

class TurmaViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Turma.
    """
    queryset = Turma.objects.all() 
    serializer_class = TurmaSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'pk'
    search_fields = ('codigo',)

class AvaliacaoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Avaliacao.
    """
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
    filter_backends = (filters.SearchFilter,)
    lookup_field = 'pk'
    search_fields = ('codigo',)

### PROFESSOR ###

@api_view(['GET'])
def professores(request):
    """
    Recupera todas as professores cadastradas
    """
    professores = Professor.objects.all()
    professores_serialized = ProfessorSerializer(professores, many=True)

    return Response(professores_serialized.data)

@api_view(['GET'])
def professor_id(request, id):
    """
    Recupera uma professor específica pelo seu id
    """
    professor = get_object_or_404(Professor, pk=id)
    professor_serialized = ProfessorSerializer(professor)

    return Response(professor_serialized.data)

@api_view(['GET'])
def pesquisar_professor(request):
    """
    Recupera uma professor de acordo com seu nome ou código
    """
    pesquisa = request.GET.get('nome')

    professor = get_object_or_404(Professor, Q(nome__icontains=pesquisa) | Q(codigo=pesquisa))
    professor_serialized = ProfessorSerializer(professor)

    return Response(professor_serialized.data)

### DEPARTAMENTO ###

@api_view(['GET'])
def departamentos(request):
    """
    Recupera todas as departamentos cadastradas
    """
    departamentos = Departamento.objects.all()
    departamentos_serialized = DepartamentoSerializer(departamentos, many=True)

    return Response(departamentos_serialized.data)

@api_view(['GET'])
def departamento_id(request, id):
    """
    Recupera uma departamento específica pelo seu id
    """
    departamento = get_object_or_404(Departamento, pk=id)
    departamento_serialized = DepartamentoSerializer(departamento)

    return Response(departamento_serialized.data)

@api_view(['GET'])
def pesquisar_departamento(request):
    """
    Recupera uma departamento de acordo com seu nome ou código
    """
    pesquisa = request.GET.get('nome')

    departamento = get_object_or_404(Departamento, Q(nome__icontains=pesquisa) | Q(codigo=pesquisa))
    departamento_serialized = DepartamentoSerializer(departamento)

    return Response(departamento_serialized.data)

### CURSOS ###

@api_view(['GET'])
def cursos(request):
    """
    Exibe todos os cursos de acordo com seu nome
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
def pesquisar_curso(request, id):
    """
    Recupera todos os cursos de um determinado departamento
    """
    pesquisa = request.GET.get('nome',)

    curso = get_object_or_404(Curso, Q(nome__icontains=pesquisa) | Q(codigo=pesquisa))
    departamento_serialized = DepartamentoSerializer(curso)

    return Response(curso_serialized.data)

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
def pesquisar_disciplina(request):
    """
    Recupera uma disciplina de acordo com seu nome ou código
    """
    pesquisa = request.GET.get('nome')

    disciplina = get_object_or_404(Disciplina, Q(nome__icontains=pesquisa) | Q(codigo=pesquisa))
    disciplina_serialized = DisciplinaSerializer(disciplina)

    return Response(disciplina_serialized.data)

### TURMA ###

@api_view(['GET'])
def turmas(request):
    """
    Recupera todas as turmas cadastradas
    """
    turmas = Turma.objects.all()
    turmas_serialized = TurmaSerializer(turmas, many=True)

    return Response(turmas_serialized.data)

@api_view(['GET'])
def turma_id(request, id):
    """
    Recupera uma turma específica pelo seu id
    """
    turma = get_object_or_404(Turma, pk=id)
    turma_serialized = TurmaSerializer(turma)

    return Response(turma_serialized.data)

@api_view(['GET'])
def pesquisar_turma(request):
    """
    Recupera uma turma de acordo com seu nome ou código
    """
    pesquisa = request.GET.get('codigo',)

    turma = get_object_or_404(Turma, Q(name__icontains=pesquisa) | Q(codigo=pesquisa))
    turma_serialized = TurmaSerializer(turma)

    return Response(turma_serialized.data)

### AVALIACAO ###

@api_view(['GET'])
def avaliacao(request):
    """
    Recupera todas as avaliacões cadastradas
    """
    avaliacoes = Avaliacao.objects.all()
    avaliacoes_serialized = AvaliacaoSerializer(avaliacoes, many=True)

    return Response(avaliacoes_serialized.data)

@api_view(['GET'])
def avaliacao_id(request, id):
    """
    Recupera uma avaliação específica pelo seu id
    """
    avaliacao = get_object_or_404(Avaliacao, pk=id)
    avaliacao_serialized = AvaliacaoSerializer(avaliacao)

    return Response(avaliacao_serialized.data)

@api_view(['GET'])
def pesquisar_avaliacao(request):
    """
    Recupera uma avaliacão de acordo com seu nome ou código
    """
    pesquisa = request.GET.get('codigo')

    avaliacao = get_object_or_404(Avaliacao, Q(nome__icontains=pesquisa) | Q(codigo=pesquisa))
    avaliacao_serialized = AvaliacaoSerializer(avaliacao)

    return Response(avaliacao_serialized.data)