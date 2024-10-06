"""This file contains the common model mixins that are to be used throughout the models."""

from django.db import models
from django.utils.timezone import datetime
from django.utils.translation import gettext_lazy as _

from mysite.utils.managers import DeletedObjectsManager, SoftDeleteManager


class SoftDeleteModelMixin(models.Model):
    """Model mixin to add functionality for soft deleteion

    It supports 3 custom managers for queryset:
        1. all_objects: Returns all objects
        2. objects: Returns objects whose `deleted_at` is null
        3. deleted_objects: Returns objects whose `deleted_at` is not null
    """

    deleted_at = models.DateTimeField(_("deleted at"), null=True, blank=True)

    all_objects = models.Manager()
    objects = SoftDeleteManager()
    deleted_objects = DeletedObjectsManager()

    class Meta:
        abstract = True

    def delete(self):
        """Soft delete instance.
        Sets `deleted_at` to current timestamp
        """
        self.deleted_at = datetime.now()
        self.save()


class CreatedUpdatedTimeModelMixin(models.Model):
    """Model mixin to add functionality for recording creation and last updation timestamp

    NOTE: It does not work with `update`. So, `update` querysets must be handled explicitly.
    """

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class BaseModel(SoftDeleteModelMixin, CreatedUpdatedTimeModelMixin):
    """Common base model.
    This adds support for soft deletion and creation and updation timestamps.
    """

    class Meta:
        abstract = True
