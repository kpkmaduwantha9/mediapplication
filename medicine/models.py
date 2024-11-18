from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    mfg_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
