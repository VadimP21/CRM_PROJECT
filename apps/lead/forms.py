"""Модуль конструктор форм приложения lead"""

from django import forms
from apps.lead.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ["first_name", "last_name", "phone", "email", "advertisement"]
