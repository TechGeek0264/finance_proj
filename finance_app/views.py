# finance_app/views.py

from django.views.generic import FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import FinanceForm
from .models import FinanceRate, FinanceCalculation

class CalculateFinanceView(FormView):
    template_name = 'finance_app/calculate_finance.html'
    form_class = FinanceForm
    success_url = reverse_lazy('calculate_finance')

    def form_valid(self, form):
        rate = form.cleaned_data['rate']
        home_value = form.cleaned_data['home_value']
        age = form.cleaned_data['age']

        # Fetch principle factor from database based on age and rate
        finance_rate = get_object_or_404(FinanceRate, age=age)
        principle_factor = getattr(finance_rate, f'rate_{rate.split(".")[0]}_{rate.split(".")[1]}')

        # Calculate principal_limit
        principal_limit = principle_factor * home_value

        # # Create FinanceCalculation object
        # calculation = FinanceCalculation.objects.create(
        #     margin=float(rate),  # Storing rate as margin for consistency with the model
        #     home_value=home_value,
        #     age=age,
        #     principal_limit=principal_limit
        # )

        result = {
            'principal_limit': principal_limit,
            'home_value': home_value,
            'age': age
        }

        return self.render_to_response(self.get_context_data(form=form, result=result))
