from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = [
            'name', 'breed', 'age', 'gender',
            'status', 'arrival_date', 'photo',
            'is_neutered', 'is_vaccinated',
            'health_status', 'description'
        ]
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
            'arrival_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        } 