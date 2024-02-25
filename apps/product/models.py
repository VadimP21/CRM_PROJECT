"""Модуль с моделями приложения product"""

from django.db.models import Model, CharField, TextField, DecimalField, BooleanField


class Product(Model):
    name = CharField(max_length=128)
    price = DecimalField(max_digits=16, decimal_places=2)
    description = TextField()
    is_active = BooleanField(default=1)

    def __str__(self):
        return f"Product(pk={self.pk}, name={self.name!r})"
