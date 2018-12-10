"""
Database Models
"""
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class CandidateInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    """
    user = models.OneToOneField(USER_MODEL)
    cnic_number = models.CharField(max_length=20, verbose_name=_("CNIC Number"))
    university = models.CharField(max_length=100)
    city = models.CharField(max_length=30, verbose_name=_("Your current Location (City)"))
    address = models.CharField(max_length=255, verbose_name=_("Permanent Address"))
    contact_number = models.CharField(max_length=30, verbose_name=_("Contact Number (s)"))
    # university = models.CharField(max_length=30)
