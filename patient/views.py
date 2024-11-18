from django.shortcuts import get_object_or_404, render, redirect
from .forms import PatientForm
from .models import Patient

def patient_home(request):
    # Fetch all patient records from the database
    patients = Patient.objects.all()
    return render(request, 'patient/patient_home.html', {'patients': patients})

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()  # Save the patient data to the database
            return redirect('patient_home')  # Redirect to patient home page
    else:
        form = PatientForm()
    return render(request, 'patient/add_patient.html', {'form': form})

def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_home')