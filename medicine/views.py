from django.shortcuts import render

# Create your views here.
def medicine_home(request):
    return render(request, 'medicine/medicine_home.html')

def add_medicine(request):
    return render(request, 'medicine/add_medicine.html')