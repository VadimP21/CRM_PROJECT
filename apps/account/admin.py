"""Модуль для админ панели приложения Account"""

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.account.models import Profile, Role

User = get_user_model()


class UserProfileInLine(admin.TabularInline):
    model = Profile


class UserNamesInline(admin.TabularInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "role",
        "is_staff",
    )
    inlines = [
        UserProfileInLine,
    ]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "password1", "password2"],
            },
        )
    ]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    inlines = [UserNamesInline]

    list_display = ("name",)
