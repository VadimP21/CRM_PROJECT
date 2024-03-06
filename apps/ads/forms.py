"""Модуль конструктор форм приложения ads"""

from django import forms
from apps.ads.models import Advertisement


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ["name", "product", "channel", "cost"]
