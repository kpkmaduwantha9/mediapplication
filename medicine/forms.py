from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'price', 'stock', 'mfg_date', 'expiry_date']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter medicine name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter stock quantity'}),
            'mfg_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
