"""crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from clientes import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clientes.urls')),

]


#*************configuracion de titulos del Admin Panel*****************
admin.site.site_header = "ITALENT COLOMBIA" # TITULO PRINCIPAL Y TITULO CAJA PASSW
admin.site.site_title = "ITALENT COLOMBIA" # PESTAÑA PAGINA WEB
admin.site.index_title ="PANEL DE ADMINISTRACION"  # PESTAÑA PAGINA / TITULO DEL PANEL