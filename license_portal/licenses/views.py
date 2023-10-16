from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.utils import timezone
from .models import License, EmailLog
from rest_framework import viewsets
from .serializers import LicenseSerializer, EmailLogSerializer

@api_view(['POST'])
def enviar_notificacion_correo(request):
    licenses_4_months = License.objects.filter(expiration_datetime__lte=timezone.now() + timezone.timedelta(days=120))
    licenses_1_month_monday = License.objects.filter(expiration_datetime__lte=timezone.now() + timezone.timedelta(days=30), expiration_datetime__gte=timezone.now(), expiration_datetime__weekday=0)
    licenses_1_week = License.objects.filter(expiration_datetime__lte=timezone.now() + timezone.timedelta(days=7))

    licenses = licenses_4_months | licenses_1_month_monday | licenses_1_week

    for license in licenses:
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
        
        EmailLog.objects.create(license_id=license.id)

    return Response({'mensaje': 'Correos enviados exitosamente'})

class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

@api_view(['GET'])
def lista_correos_enviados(request):
    correos_enviados = EmailLog.objects.all()
    serializer = EmailLogSerializer(correos_enviados, many=True)
    return Response(serializer.data)