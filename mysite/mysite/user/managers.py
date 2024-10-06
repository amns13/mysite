from django.contrib.auth.models import UserManager
from django.db.models import QuerySet


class SoftDeletedUserManager(UserManager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(deleted_at__isnull=True)
