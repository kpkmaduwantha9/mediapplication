from django.urls import path
from . import views

urlpatterns=[
    path ('patienthome/', views.patient_home, name = 'patient_home'),
    path ('addpatient/', views.add_patient, name = 'add_patient'),

]