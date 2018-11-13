from rest_framework import viewsets
from .serializers import DepartamentoSerializer
from .models import Departamento


class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar e editar Departamentos.
    """
    queryset = Departamento.objects.all().order_by('-nome')
    serializer_class = DepartamentoSerializer