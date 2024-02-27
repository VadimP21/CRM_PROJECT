"""Модуль с моделями приложения product"""

from django.db.models import Model, CharField, TextField, DecimalField, BooleanField


class Product(Model):
    #  TODO сделать primary_key is name
    name = CharField(max_length=128, verbose_name="Название")
    price = DecimalField(max_digits=16, decimal_places=2, verbose_name="Стоимость")
    description = TextField(verbose_name="Описание")
    is_active = BooleanField(default=1, verbose_name="Активен")

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"
