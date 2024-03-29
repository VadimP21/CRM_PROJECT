"""Модуль с моделями приложения product"""

from django.db.models import Model, CharField, TextField, DecimalField, BooleanField


class Product(Model):
    name = CharField(primary_key=True, max_length=128, verbose_name="Название")
    price = DecimalField(max_digits=16, decimal_places=2, verbose_name="Стоимость")
    description = TextField(verbose_name="Описание")
    archived = BooleanField(default=0, verbose_name="В архиве")

    def __str__(self):
        return f"Product {self.name!r}"
