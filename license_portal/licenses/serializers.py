from rest_framework import serializers
from .models import License, EmailLog

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['client', 'package', 'license_type', 'created_datetime', 'expiration_datetime']

class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = ['sent_at', 'license_id']

class EmailNotificationSerializer(serializers.Serializer):
    client_id = serializers.IntegerField()
    license_id = serializers.IntegerField()