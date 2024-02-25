"""Модуль для админ панели приложения Account"""

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from apps.account.models import Profile, Role, RolePermission

User = get_user_model()


class UserProfileInLine(admin.TabularInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    inlines = [UserProfileInLine]
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["username", "email", "password1", "password2"],
            },
        )
    ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "role")
    ordering = (
        "pk",
        "user",
        "role",
    )
    search_fields = "role", "user"

    def get_queryset(self, request):
        return Profile.objects.select_related("user").select_related("role")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )


@admin.register(RolePermission)
class RolePermissionAdmin(admin.ModelAdmin):
    list_display = ("pk", "role", "permission")
