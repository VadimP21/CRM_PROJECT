from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from apps.account.models import Profile, Role


@receiver(m2m_changed, sender=Role.permissions.through)
def update_users_permissions(sender, instance, action, **kwargs):
    if action == "post_add" or action == "post_remove":
        # Для добавления или удаления разрешений
        users_to_update = Profile.objects.filter(role=instance)
        for profile in users_to_update:
            profile.user.user_permissions.clear()
            for permission in instance.permissions.all():
                profile.user.user_permissions.add(permission)
