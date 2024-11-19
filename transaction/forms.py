

## forms.py
from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['patient', 'medicine', 'quantity']
        widgets = {
            'patient': forms.Select(),
            'medicine': forms.Select(),
        }

    quantity = forms.IntegerField(min_value=1, required=True)


