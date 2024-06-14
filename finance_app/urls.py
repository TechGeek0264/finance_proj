# finance_app/urls.py

from django.urls import path
from .views import CalculateFinanceView

urlpatterns = [
    path('', CalculateFinanceView.as_view(), name='calculate_finance'),
]
