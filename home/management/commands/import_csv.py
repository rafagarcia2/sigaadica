from django.core.management.base import BaseCommand, CommandError
from import_export import resources
from home.models import Professor, Disciplina
from tablib import Dataset
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

class Command(BaseCommand):
    help = """ Recupera os arquivos csv e importa seus dados para os models."""

    def handle(self, *args, **options):
        if len(args) > 0:
            raise CommandError("Nenhum argumento é necessário")

        path = os.path.abspath('./data')

        if os.path.exists(path):
            csvs = os.listdir(path)

            for csv_file in csvs:
                path_file = os.path.join(path, csv_file)

                dataset = Dataset()

                dataset.load(open(path_file).read())

                csv_class = globals()[csv_file.split('.')[0].capitalize() + 'Resource']
                csv_object = csv_class()
                result = csv_object.import_data(dataset, dry_run=True)

                if not result.has_errors():
                    csv_class().import_data(dataset, dry_run=False)
        else:
            print("Pasta com os dados não encontrada. Nenhuma ação foi feita")