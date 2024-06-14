from django.test import TestCase

# Create your tests here.
# finance_app/tests.py

from django.test import TestCase
from django.urls import reverse
from .models import FinanceCalculation
from .forms import FinanceForm

class FinanceCalculationTests(TestCase):

    def test_finance_model_creation(self):
        calculation = FinanceCalculation.objects.create(
            margin=0.05,
            home_value=314000,
            age=65,
            initial_rate=5.99,
            expected_rate=5.01,
            cap_on_interest_rate=10.99,
            initial_loc_growth=6.49,
            principal_limit=150000
        )
        self.assertEqual(FinanceCalculation.objects.count(), 1)
        # Add more assertions as needed

class FinanceFormTests(TestCase):

    def test_finance_form_valid(self):
        form_data = {
            'margin': 0.05,
        }
        form = FinanceForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_finance_form_invalid(self):
        form_data = {
            'margin': -0.05,  # Invalid margin value
        }
        form = FinanceForm(data=form_data)
        self.assertFalse(form.is_valid())

class FinanceViewTests(TestCase):

    def test_calculate_finance_view(self):
        url = reverse('calculate_finance')
        data = {
            'margin': 0.05,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Results')
        # Add more assertions to check the response content

    def test_calculate_finance_view_invalid_form(self):
        url = reverse('calculate_finance')
        data = {
            'margin': -0.05,  # Invalid margin value
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Results')
        # Add more assertions to check for error handling

