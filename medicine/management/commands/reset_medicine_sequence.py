from django.core.management.base import BaseCommand
from django.db import connection
from medicine.models import Medicine

class Command(BaseCommand):
    help = 'Delete all Medicine records and reset the ID sequence'

    def handle(self, *args, **kwargs):
        # Delete all records
        Medicine.objects.all().delete()

        # Reset the auto-increment sequence
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='medicine_medicine';")

        self.stdout.write(self.style.SUCCESS("All Medicine records deleted and ID sequence reset."))
