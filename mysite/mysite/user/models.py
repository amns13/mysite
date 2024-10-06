from django.contrib.auth.models import AbstractUser

from mysite.user.managers import SoftDeletedUserManager
from mysite.utils.models import BaseModel


class User(BaseModel, AbstractUser):
    """Custom user model.
    It adds soft delte and create/update tracking to Django's abstract user model.
    """

    objects = SoftDeletedUserManager()
