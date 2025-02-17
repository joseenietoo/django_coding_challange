"""licenses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include 
from django.contrib import admin
from rest_framework import routers
from licenses import views

router = routers.DefaultRouter()
router.register(r'licenses', views.LicenseViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)), 
    url(r'^api/licenses/enviar_notificacion_correo/$', views.enviar_notificacion_correo, name='enviar_notificacion_correo'),
    url(r'^api/licenses/lista_correos_enviados/(?P<cantidad>\d+)/$', views.lista_correos_enviados, name='lista_correos_enviados'),
    url(r'^api/licenses/resumen_notificaciones/$', views.resumen_notificaciones, name='resumen_notificaciones'),
    path('frontend/', TemplateView.as_view(template_name='frontend/index.html')),
]
