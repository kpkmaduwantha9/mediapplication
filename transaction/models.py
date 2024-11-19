from django.db import models
from patient.models import Patient  
from medicine.models import Medicine  

class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  
    quantity = models.IntegerField() 

    def __str__(self):
        return f"Transaction for {self.patient.name} - {self.medicine.name} (Quantity: {self.quantity})"
