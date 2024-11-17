from django.shortcuts import render

# Create your views here.

def patient_home(request):
    return render(request, 'patient/patient_home.html')  

def add_patient(request):
    return render(request, 'patient/add_patient.html')  
