from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class MyAdminSite(AdminSite):
    admin.site.register(SectorEconomico)
    admin.site.register(Empresa)
    admin.site.register(Contactos)
    admin.site.register(paises)
    admin.site.register(departamentos)
    admin.site.register(ciudades)

#class CandidateResource(resources.ModelResource):
#    class Meta:
#        model = Candidato



# Register your models here.
#class CandidateAdmin(ImportExportModelAdmin):
#    resource_class = CandidateResource
#admin.site.register(Candidato, CandidateAdmin)
#admin.site.register(Postulados)
