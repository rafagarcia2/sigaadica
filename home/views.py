from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .serializers import DepartamentoSerializer, CursoSerializer
from .models import Departamento, Curso


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