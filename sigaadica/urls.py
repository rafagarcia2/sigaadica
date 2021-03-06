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
from home.views import DisciplinaViewSet, DepartamentoViewSet, curso_id, disciplinas, disciplina_id, pesquisa_disciplina

router = routers.DefaultRouter()
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path('cursos/<int:id>', curso_id),
    path('disciplina', disciplinas),
    path('disciplina/<int:id>', disciplina_id),
    path('disciplina/buscar', pesquisa_disciplina),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
