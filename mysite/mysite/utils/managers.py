"""This file contains custom base manager mixins to be reused throughout the app"""

from django.db import models


class SoftDeleteManager(models.Manager):
    """Manager for returning only non-deleted objects"""

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(deleted_at__isnull=True)


class DeletedObjectsManager(models.Manager):
    """Manager for returning only deleted objects"""

    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().exclude(deleted_at__isnull=True)
