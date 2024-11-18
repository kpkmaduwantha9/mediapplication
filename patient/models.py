from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    nic = models.CharField(max_length=12)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    problem = models.TextField()

    def __str__(self):
        return self.name
