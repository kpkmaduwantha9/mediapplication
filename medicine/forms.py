from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'price', 'stock', 'mfg_date', 'expiry_date']


mfg_date = forms.DateField(input_formats=['%Y-%m-%d'])
expiry_date = forms.DateField(input_formats=['%Y-%m-%d'])