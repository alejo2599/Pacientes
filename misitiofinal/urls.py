"""misitiofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
#from proyectoFinal.views import IndexView

admin.autodiscover()

urlpatterns = [
	#url(r'^$', IndexView.as_view()), 
    url(r'^$', 'proyectoFinal.views.inicio'), 
    url(r'^usuarios/$', 'proyectoFinal.views.usuarios'),    
    url(r'^sobre/$', 'proyectoFinal.views.sobre'),
    url(r'^pacientes/$', 'proyectoFinal.views.lista_pacientes'),    
    url(r'^paciente/(?P<id_paciente>\d+)$','proyectoFinal.views.detalle_paciente'), 

    url(r'^admin/doc', include('django.contrib.admindocs.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),

    url(r'^contacto/$','proyectoFinal.views.contacto'),
    url(r'^paciente/nuevo/$','proyectoFinal.views.nuevo_paciente'),
    url(r'^comenta/$','proyectoFinal.views.nuevo_comentario'),
    url(r'^usuario/nuevo$','proyectoFinal.views.nuevo_usuario'),
    url(r'^ingresar/$','proyectoFinal.views.ingresar'),
    url(r'^privado/$','proyectoFinal.views.privado'),
    url(r'^cerrar/$','proyectoFinal.views.cerrar_sesion'),
]
