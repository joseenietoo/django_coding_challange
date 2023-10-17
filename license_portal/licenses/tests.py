from django.test import TestCase
from licenses.models import License, Client, EmailLog

class LicenseModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            client_name="Test Client",
            poc_contact_name="Test Contact",
            poc_contact_email="test@example.com",
            admin_poc=None
        )
        self.license = License.objects.create(
            client=self.client,
            package=0,
            license_type=0
        )

    def test_license_creation(self):
        self.assertEqual(self.license.client, self.client)
        self.assertEqual(self.license.package, 0)
        self.assertEqual(self.license.license_type, 0)

class ClientModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            client_name="Test Client",
            poc_contact_name="Test Contact",
            poc_contact_email="test@example.com",
            admin_poc=None
        )

    def test_client_creation(self):
        self.assertEqual(self.client.client_name, "Test Client")
        self.assertEqual(self.client.poc_contact_name, "Test Contact")
        self.assertEqual(self.client.poc_contact_email, "test@example.com")

class EmailLogModelTest(TestCase):
    def setUp(self):
        self.client = Client.objects.create(
            client_name="Test Client",
            poc_contact_name="Test Contact",
            poc_contact_email="test@example.com",
            admin_poc=None
        )
        self.license = License.objects.create(
            client=self.client,
            package=0,
            license_type=0
        )
        self.email_log = EmailLog.objects.create(
            sent_at=None,
            license_id=self.license.id
        )

    def test_email_log_creation(self):
        self.assertEqual(self.email_log.license_id, self.license.id)

