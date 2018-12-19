from django.core.management.base import BaseCommand, CommandError
from import_export import resources
from home.models import Professor, Disciplina, Turma
from tablib import Dataset
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
import os

class DisciplinaResource(resources.ModelResource):
    class Meta:
        model = Disciplina

    def get_instance(self, instance_loader, row):
        return False

class ProfessorResource(resources.ModelResource):
    class Meta:
        model = Professor

    def get_instance(self, instance_loader, row):
        return False

class TurmaResource(resources.ModelResource):
    # disciplina_id = Field(
    #     column_name='id_componente',
    #     attribute='disciplina_id',
    #     widget=ForeignKeyWidget(Disciplina, 'id_componente')
    # )

    disciplina_id = Field(
        column_name='id_componente',
        attribute='disciplina',
        widget=ForeignKeyWidget(Disciplina, 'id_componente')
    )

    class Meta:
        model = Turma

        # fields = ('disciplina__id_componente',)
        skip_unchanged = True
        report_skipped = False

    def get_instance(self, instance_loader, row):
        return False

class Command(BaseCommand):
    help = """ Recupera os arquivos csv e importa seus dados para os models."""

    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError("Nenhum argumento é necessário")

        path = os.path.abspath('./data')

        if os.path.exists(path):
            # csvs = os.listdir(path)
            csvs = ['professor.csv', 'disciplina.csv', 'turma.csv']
            # csvs = ['turma.csv']
            for csv_file in csvs:
                path_file = os.path.join(path, csv_file)

                # if csv_file == 'turma.csv':
                #     print(open(path_file).read())

                dataset = Dataset()

                dataset.load(open(path_file).read())
                print(dataset)
                csv_class = globals()[csv_file.split('.')[0].capitalize() + 'Resource']
                csv_object = csv_class()
                result = csv_object.import_data(dataset, dry_run=True, raise_errors=True)

                if not result.has_errors():
                    csv_class().import_data(dataset, dry_run=False)
        else:
            print("Pasta com os dados não encontrada. Nenhuma ação foi feita")