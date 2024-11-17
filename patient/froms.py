from django import forms

class PatientForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    Gender = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    