from django.urls import path
from . import views

urlpatterns = [
    path('patienthome/', views.patient_home, name='patient_home'),  
    path('addpatient/', views.add_patient, name='add_patient'),     
    path('delete_patient/<int:id>/', views.delete_patient, name='delete_patient'),
    path('edit_patient/<int:id>/', views.edit_patient, name='edit_patient'),
]
