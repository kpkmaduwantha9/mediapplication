from django.shortcuts import redirect, render
from .models import Medicine
from .forms import MedicineForm
from django.shortcuts import render, get_object_or_404


# Create your views here.
def medicine_home(request):
    return render(request, 'medicine/medicine_home.html')

def add_medicine(request):
    return render(request, 'medicine/add_medicine.html')

from .forms import MedicineForm

def medicine_home(request):
    products = Medicine.objects.all()  # Fetch all medicines from the database
    return render(request, 'medicine/medicine_home.html', {'products': products})

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine-home')  # Corrected to redirect to 'medicine-home'
    else:
        form = MedicineForm()
    return render(request, 'medicine/add_medicine.html', {'form': form})

def edit_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    # Add your logic to handle the edit form or rendering the edit page
    return render(request, 'medicine/edit_medicine.html', {'medicine': medicine})

def delete_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    medicine.delete()
    return redirect('medicine_home')  # Redirect back to the home page or wherever you want

def edit_medicine(request, id):
    medicine = get_object_or_404(Medicine, id=id)
    
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('medicine_list')  
    else:
        form = MedicineForm(instance=medicine)
    
    return render(request, 'medicine/edit_medicine.html', {'form': form})

from django.shortcuts import render
from .models import Medicine


def medicine_list(request):
    products = Medicine.objects.all()  # Fetch all medicines from the database
    return render(request, 'medicine/medicine_home.html', {'products': products})