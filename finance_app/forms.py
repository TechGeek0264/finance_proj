# finance_app/forms.py

from django import forms
from .models import FinanceRate

class FinanceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Fetch rate choices from FinanceRate model
        self.fields['rate'].choices = FinanceRate.RATE_CHOICES
        
        # Fetch distinct age choices from FinanceRate model
        age_choices = FinanceRate.objects.values_list('age', flat=True).distinct().order_by('age')
        self.fields['age'].choices = [(age, age) for age in age_choices]
    
    rate = forms.ChoiceField(
        label='Rate',
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    age = forms.ChoiceField(
        label='Age',
        choices=[],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    home_value = forms.FloatField(
        label='Home Value', 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
