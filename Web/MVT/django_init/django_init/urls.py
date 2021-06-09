"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from apps.pricipal.views import inicio,crear,editar_persona,eliminar_persona,index,readCiudad,crearCiudad,eliminarciudad,editarciudad

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('read/',inicio,name='inicio'),
    path('crear/',crear,name='crear_persona'),
    path('editar_persona/<int:id>/',editar_persona,name='editar_persona'),
    path('eliminar_persona/<int:id>/',eliminar_persona,name='eliminar_persona'),
    path('readciudad/',readCiudad,name='readciudad'),
    path('crearciudad/',crearCiudad,name='crearciudad'),
    path('editarciudad/<int:id>',editarciudad,name='editarciudad'),
    path('eliminarciudad/<int:id>/',eliminarciudad,name='eliminarciudad')
   

    ]
