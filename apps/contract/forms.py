"""Модуль конструктор форм приложения contract"""

from django import forms
from apps.contract.models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ["name", "product", "file", "start_date", "end_date", "cost"]
