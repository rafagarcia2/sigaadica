from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DepartamentoSerializer, CursoSerializer
from .models import Departamento, Curso


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar e editar Departamentos.
    """
    queryset = Departamento.objects.all().order_by('-nome')
    serializer_class = DepartamentoSerializer



### CURSOS ###

@api_view(['GET'])
def curso(request):
    """
    View responsável por exibir todos os cursos
    """
    cursos_serializer = CursoSerializer(Curso.objects.all(), many=True)
    return Response(cursos_serializer.data)


@api_view(['GET'])
def curso_id(request, id):
    """
    View responsável por devolver um curso específico pelo seu id
    """
    try:
        curso = Curso.objects.get(id=id)
        curso_serialzer = CursoSerializer(curso)

        return Response(curso_serialzer.data)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def curso_por_departamento(request, id):
    """
    View responsável por pegar todos os cursos de um determinado departamento
    """
    pass