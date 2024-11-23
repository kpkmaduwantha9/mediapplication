from django.core.management.base import BaseCommand
from django.db import connection
from patient.models import Patient

class Command(BaseCommand):
    help = 'Delete all Patient records and reset the ID sequence'

    def handle(self, *args, **kwargs):
        # Delete all records
        Patient.objects.all().delete()

        # Reset the auto-increment sequence
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='patient_patient';")

        self.stdout.write("All Patient records deleted and ID sequence reset.")
