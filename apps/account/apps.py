"""Конфигурация приложения accounts"""

from django.apps import AppConfig



class AccountConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.account"

    def ready(self):
        from apps.account.signals.permissions_signal import update_users_permissions
