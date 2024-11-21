from django.db import models
from patient.models import Patient  
from medicine.models import Medicine  
from django.utils.timezone import now

class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)  
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  
    quantity = models.IntegerField() 
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"Transaction for {self.patient.name} - {self.medicine.name} (Quantity: {self.quantity})"
