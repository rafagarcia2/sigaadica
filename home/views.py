from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import DepartamentoSerializer, CursoSerializer, DisciplinaSerializer
from .models import Departamento, Curso, Disciplina


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    Visualiza e edita Departamentos.
    """
    queryset = Departamento.objects.all().order_by('-nome')
    serializer_class = DepartamentoSerializer



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