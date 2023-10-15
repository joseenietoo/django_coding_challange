from rest_framework import viewsets
from .models import License
from .serializers import LicenseSerializer

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

    def enviar_notificacion_por_correo(self):
        license = self.get_object()

        if (
            (license.expiration_datetime - timezone.now()).days == 120
            or
            (license.expiration_datetime - timezone.now()).days <= 30 and timezone.now().weekday() == 0
            or
            (license.expiration_datetime - timezone.now()).days <= 7
        ):
            cuerpo_correo = f"""
                Información de Licencia:

                ID de Licencia: {license.id}
                Tipo de Licencia: {license.license_type}
                Nombre del Paquete: {license.package.get_display_name()}
                Fecha de Expiración: {license.expiration_datetime}
                Cliente POC: {license.client.client_poc_name} ({license.client.client_poc_email})
            """

            send_mail(
                'Notificación de Expiración de Licencia',
                cuerpo_correo,
                'jose.nietov1@mayor.cl',  
                ['jose.nietov1@mayor.cl'],
                fail_silently=False,
            )
