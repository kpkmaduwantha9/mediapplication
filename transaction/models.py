from django.db import models
from patient.models import Patient  # Import Patient model from patient app
from medicine.models import Medicine  # Import Medicine model from medicine app

class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  # Reference Patient model
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  # Reference Medicine model
    quantity = models.IntegerField()  # Quantity of the medicine in the transaction

    def __str__(self):
        return f"Transaction for {self.patient.name} - {self.medicine.name} (Quantity: {self.quantity})"
