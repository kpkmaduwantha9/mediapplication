from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from patient.models import Patient
from medicine.models import Medicine
from .models import Transaction

def add_transaction(request):
    if request.method == 'POST':
        # Get form data
        patient_id = request.POST.get('patient')
        medicine_id = request.POST.get('medicine')
        quantity = request.POST.get('quantity')

        # Check if all required fields are filled
        if not patient_id or not medicine_id or not quantity:
            messages.error(request, "All fields are required, including the quantity.")
            return redirect('add_transaction')

        # Validate and convert IDs to integers
        try:
            patient_id = int(patient_id)
            medicine_id = int(medicine_id)
        except ValueError:
            messages.error(request, "Invalid patient or medicine ID. Please ensure correct data is entered.")
            return redirect('add_transaction')

        try:
            # Get Patient and Medicine instances
            patient = Patient.objects.get(id=patient_id)
            medicine = Medicine.objects.get(id=medicine_id)
        except Patient.DoesNotExist:
            messages.error(request, "Patient with the specified ID does not exist.")
            return redirect('add_transaction')
        except Medicine.DoesNotExist:
            messages.error(request, "Medicine with the specified ID does not exist.")
            return redirect('add_transaction')

        # Validate quantity
        try:
            quantity = int(quantity)
            if quantity <= 0:
                messages.error(request, "Quantity must be a positive integer.")
                return redirect('add_transaction')
        except ValueError:
            messages.error(request, "Invalid quantity value. Please enter a valid number.")
            return redirect('add_transaction')

        # Create and save the transaction
        transaction = Transaction(
            patient=patient,  # Ensure this is a valid Patient instance
            medicine=medicine,  # Ensure this is a valid Medicine instance
            quantity=quantity
        )
        transaction.save()

        # Redirect to a success page with a success message
        messages.success(request, "Transaction added successfully.")
        return redirect('transaction_success')

    # If it's a GET request, fetch all patients and medicines to show in the form
    patients = Patient.objects.all()
    medicines = Medicine.objects.all()

    return render(request, 'transaction/add_transaction.html', {
        'patients': patients,
        'medicines': medicines
    })

def transaction_success(request):
    # You can render a success template or return a simple message
    return render(request, 'transaction/success.html')