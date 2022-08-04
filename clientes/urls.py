from django.urls import path
from . import views
from proyectovacantes import views as viewspv
#from candidatos import views as viewscan
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.generic.base import RedirectView




urlpatterns = [
    path('', views.login_view, name='login'),
    path('', views.logout_view, name='logout'),

    #*******************crud clientes*****************
    path('clienteslistar',views.clienteslistar, name='clienteslistar'),
    path('clientescrear',views.clientescrear, name='clientescrear'), #ok
    path('clienteseliminar/<int:id>',views.clienteseliminar, name='clienteseliminar'),  
    path('clienteseditar/<int:id>',views.clienteseditar, name='clienteseditar'),  
    path('SectorEconomicocrear',views.SectorEconomicocrear, name='SectorEconomicocrear'), #ok  
   
    #*******************crud contactos*****************
    path('contactolistar',views.contactolistar, name='contactolistar'),
    path('contactocrear',views.contactocrear, name='contactocrear'), #ok
    path('contactoeliminar/<int:id>',views.contactoeliminar, name='contactoeliminar'),
    path('contactoeditar/<int:id>',views.contactoeditar, name='contactoeditar'),



    
#****************************VACANTES*************************
    path('vacantelistar', viewspv.vacantelistar, name='vacantelistar'),
    path('vacantecrear', viewspv.vacantecrear, name='vacantecrear'),
    path('vacanteeditar/<int:id>',viewspv.vacanteeditar, name='vacanteeditar'),
    path('vacanteeliminar/<int:id>',viewspv.vacanteeliminar, name='vacanteeliminar'),
    path('vacanteeditar', viewspv.addarchivovacante, name='addarchivovacante'),

    #path('vacantegestionar/<str:pk_test>/', viewspv.vacantegestionar, name='vacantegestionar'),
   # path('candidatoasignar', viewspv.candidatoasignar, name='candidatoasignar'),
   # path('candidatocontactabilidad', viewspv.candidatocontactabilidad, name='candidatocontactabilidad'),

#***************************antecedentes****************************
    path('policia', viewspv.policia, name='policia'),
    path('procuraduria', viewspv.procuraduria, name='procuraduria'),
    path('contraloria', viewspv.contraloria, name='contraloria'),
    path('performance', viewspv.performance, name='performance'),
    path('portada', viewspv.portada, name='portada'),
    path('grafica', viewspv.grafica, name='grafica'),
   
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

