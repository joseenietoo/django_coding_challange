""" Data model for licenses application
"""
import enum

from datetime import timedelta, datetime
from typing import Tuple, List

from django.contrib.auth.models import User
from django.db import models

LICENSE_EXPIRATION_DELTA = timedelta(days=90)


class ChoiceEnum(enum.Enum):
    """Enum for choices in a choices field"""
    @classmethod
    def get_choices(cls) -> List[Tuple[str, int]]:
        return [(a.name, a.value) for a in cls]


class Package(ChoiceEnum):
    """A Package accessible to a client with a valid license"""
    javascript_sdk = 0
    ios_sdk = 1
    android_sdk = 2


class LicenseType(ChoiceEnum):
    """A license type"""
    production = 0
    evaluation = 1


def get_default_license_expiration() -> datetime:
    """Get the default expiration datetime"""
    return datetime.utcnow() + LICENSE_EXPIRATION_DELTA


class License(models.Model):
    """ Data model for a client license allowing access to a package
    """
    client = models.ForeignKey('licenses.Client', on_delete=models.CASCADE)
    package = models.PositiveSmallIntegerField(choices=Package.get_choices())
    license_type = models.PositiveSmallIntegerField(choices=LicenseType.get_choices())

    created_datetime = models.DateTimeField(auto_now=True)
    expiration_datetime = models.DateTimeField(default=get_default_license_expiration)

    class Meta:
        app_label = 'licenses'

class Client(models.Model):
    """ A client who holds licenses to packages
    """
    client_name = models.CharField(max_length=120, unique=True)
    poc_contact_name = models.CharField(max_length=120)
    poc_contact_email = models.EmailField()

    admin_poc = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE)

class EmailLog(models.Model):
    sent_at = models.DateTimeField(auto_now_add=True)
    license_id = models.IntegerField()

    def __str__(self):
        return f'Email enviado el {self.sent_at} para la licencia ID {self.license_id}'