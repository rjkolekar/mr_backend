# authentication/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    name = models.CharField(_('name'), max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    contact_number = models.CharField(_('contact number'), max_length=15, validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])
    profile_picture = models.ImageField(_('profile picture'), upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.username
