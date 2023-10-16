from django.test import TestCase
from .models import EmailLog

class EmailLogTests(TestCase):
    def test_creacion_email_log(self):
        email_log = EmailLog.objects.create(license_id=1)
        self.assertEqual(email_log.license_id, 1)
