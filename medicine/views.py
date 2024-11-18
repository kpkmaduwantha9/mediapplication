from django.shortcuts import redirect, render
from .forms import MedicineForm

# Create your views here.
def medicine_home(request):
    return render(request, 'medicine/medicine_home.html')

def add_medicine(request):
    return render(request, 'medicine/add_medicine.html')

def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicine_home')  # Adjust as per your navigation
    else:
        form = MedicineForm()
    return render(request, 'medicine/add_medicine.html', {'form': form})