"""sigaadica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from home.views import professor_id, professores, pesquisar_professor
from home.views import departamento_id, departamentos, pesquisar_departamento
from home.views import curso_id, cursos, pesquisar_curso
from home.views import disciplina_id, disciplinas, pesquisar_disciplina
from home.views import turma_id, turmas, pesquisar_turma
from home.views import ProfessorViewSet
from home.views import DepartamentoViewSet 
from home.views import CursoViewSet
from home.views import DisciplinaViewSet
from home.views import TurmaViewSet
from home.views import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'professores', ProfessorViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'avaliacoes', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('professor', professores),
    path('departamento', departamentos),
    path('curso', cursos) ,
    path('disciplina', disciplinas),
    path('turma', turmas),
    path('professor/<int:id>', professor_id),
    path('departamento/<int:id>',departamento_id),
    path('curso/<int:id>', curso_id),
    path('disciplina/<int:id>', disciplina_id),
    path('turma/<int:id>', turma_id),
    path('professor/buscar', pesquisar_professor),
    path('departamento/buscar', pesquisar_departamento),
    path('curso/buscar', pesquisar_curso),
    path('disciplina/buscar', pesquisar_disciplina),
    path('turma/buscar', pesquisar_turma),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
       
]
