"""
URL configuration for M6_AE2_ind project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aplicacion_2.views import primeraFuncion
from aplicacion_2.views import formularioContacto
from aplicacion_2.views import informeUsuarios
from aplicacion_2.views import registroProveedores
from aplicacion_2.views import informeProveedores

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeraFuncion, name = 'index'),
    path('registro/', formularioContacto, name = 'registro'),
    path('salida/', informeUsuarios, name = 'salida'),
    path('registro_empresa/', registroProveedores, name = 'registro_empresa'),
    path('salida_empresas/', informeProveedores, name = 'salida_empresas'),
]

