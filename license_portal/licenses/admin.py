from django.contrib import admin
from .models import EmailLog, License

admin.site.register(EmailLog)
admin.site.register(License)
