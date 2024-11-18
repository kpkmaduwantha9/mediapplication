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


def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    
    if request.method == 'POST':
        patient.name = request.POST.get('name')
        patient.nic = request.POST.get('nic')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.problem = request.POST.get('problem')
        patient.save()
        return redirect('patient_home')  # Redirect to the patient list after editing

    return render(request, 'patient/edit_patient.html', {'patient': patient})
