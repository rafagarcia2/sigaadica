from django.contrib import admin
from .models import Departamento, Turma, Disciplina

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']


class TurmaAdmin(admin.ModelAdmin):
	search_fields = ['codigo']
	list_filter = ['codigo']


class DisciplinaAdmin(admin.ModelAdmin):
	list_display = ['id_componente', 'codigo', 'nome']
	search_fields = ['id_componente', 'codigo']
	list_filter = ['codigo']

admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Turma, TurmaAdmin)