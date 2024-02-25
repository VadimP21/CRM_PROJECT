"""Модуль для админ панели приложения Core"""

from django.contrib.admin import ModelAdmin, action, register
from django.core.cache import cache

from apps.core.models import SiteSettings


@register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    actions = ["clear_cache", "load_config"]

    @action(description="Очистить кэш")
    def clear_cache(self, *args, **kwargs):
        cache.clear()

    @action(description="Загрузить настройки")
    def load_config(self, *args, **kwargs):
        SiteSettings.load_config()

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            SiteSettings.load().save()
        except Exception:
            pass
