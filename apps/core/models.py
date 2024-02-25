"""Модуль с моделями приложения core"""

from json import loads

from django.db.models import BooleanField, Model, PositiveIntegerField


class SiteSettings(Model):
    cache_active = BooleanField(default=False,)
    cache_time = PositiveIntegerField(
        default=60 * 60 * 24, )  # sec*min*hor

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        if not self.cache_active:
            self.cache_time = 0
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()

    @staticmethod
    def load_config():
        with open("core/config/config.json", "r") as cfg:
            data = loads(cfg.read())
            model = SiteSettings.objects.get()
            model.cache_active = data["cache_active"]
            model.cache_time = data["cache_time"]
            model.save()

    def __str__(self):
        return "Настройки сайта"
