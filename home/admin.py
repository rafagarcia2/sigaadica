from django.contrib import admin
from .models import Professor, Departamento, Curso, Disciplina, Turma, Avaliacao

class ProfessorAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']
 
admin.site.register(Professor, ProfessorAdmin,)

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']

admin.site.register(Departamento, DepartamentoAdmin,)

class CursoAdmin(admin.ModelAdmin):
	list_display = ['departamento', 'codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']
 
admin.site.register(Curso, CursoAdmin,)

class DisciplinaAdmin(admin.ModelAdmin):
	list_display = ['departamento', 'codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']
 
admin.site.register(Disciplina, DisciplinaAdmin,)

class TurmaAdmin(admin.ModelAdmin):
	list_display = [
		'professor',
        'disciplina',
        'codigo', 
        'qnt_discentes',
        'tx_aprov',
        'media_turma',
        'qnt_tranc',
        'aprov_prim',]
	search_fields = ['codigo']
	list_filter = ['professor','disciplina']
 
admin.site.register(Turma, TurmaAdmin,)

class AvaliacaoAdmin(admin.ModelAdmin):
	list_display = ['turma', 'codigo', 'auto_avaliacao','post_prof']
	search_fields = ['codigo']
	list_filter = ['turma']
 
admin.site.register(Avaliacao, AvaliacaoAdmin,)