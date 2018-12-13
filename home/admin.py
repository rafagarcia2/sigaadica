from django.contrib import admin
from .models import Departamento

class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['codigo', 'nome']
	search_fields = ['codigo']
	list_filter = ['nome']
	
admin.site.register(Departamento, DepartamentoAdmin)