from django.test import TestCase
from licenses.models import License, Client, EmailLog

class EnviarNotificacionCorreoTest(TestCase):
    def test_enviar_notificacion_correo(self):
        client = Client.objects.create(
            client_name="Ejemplo Cliente",
            poc_contact_name="Ejemplo Contacto",
            poc_contact_email="ejemplo@example.com",
            admin_poc=1
        )
        license = License.objects.create(
            client=client,
            package=0,
            license_type=0,
            expiration_datetime="2023-12-31T23:59:59Z" 
        )

        response = self.client.post('/api/licenses/enviar_notificacion_correo/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'mensaje': 'Correos enviados exitosamente'})

class ListaCorreosEnviadosTest(TestCase):
    def test_lista_correos_enviados(self):
        client = Client.objects.create(
            client_name="Ejemplo Cliente 2",
            poc_contact_name="Ejemplo Contacto 2",
            poc_contact_email="ejemplo2@example.com",
            admin_poc=1
        )
        license = License.objects.create(
            client=client,
            package=0,
            license_type=0,
            expiration_datetime="2023-12-31T23:59:59Z"
        )
        email_log = EmailLog.objects.create(
            sent_at=None,
            license_id=license.id
        )

        response = self.client.get('/api/licenses/lista_correos_enviados/5/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

class ResumenNotificacionesTest(TestCase):
    def test_resumen_notificaciones(self):
        response = self.client.get('/api/licenses/resumen_notificaciones/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('total_correos_enviados', response.data)