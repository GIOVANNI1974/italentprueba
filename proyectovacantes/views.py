#from pyexpat.errors import messages
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from crispy_forms.utils import render_crispy_form
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from .models import *
from proyectovacantes.forms import *
from clientes.forms import *
from clientes.models import *
from .forms import VacanteForm
from .forms import *
#from candidatos.models import Candidato, Postulados
#from candidatos.forms import *
#from candidatos.filters import *
from django_filters import rest_framework as filters
#from .forms import *
from django.contrib.staticfiles import finders
#from .filters import *
from django.db.models.functions import Concat
from django.contrib.auth.models import User
from datetime import datetime


#result = finders.find('js/datagrid.min.js')
#searched_locations = finders.searched_locations


# Create your views here.
def vacantelistar(request):
    vacantes = Vacante.objects.all()
    return render(request, 'crud_Vacantes/listar.html', {'vacantes': vacantes}) 
    #return HttpResponse("<h1>Bienvenido a la libreria</h1>")




def vacantecrear(request):
    formulariovc = VacanteCrearForm(request.POST or None, request.FILES or None)
    if formulariovc.is_valid():
        formulariovc.save()
        print(formulariovc)
        return redirect('clienteslistar')
    return render(request, 'crud_Vacantes/crear.html', {'formulariovc': formulariovc})
    #return HttpResponse("<h1>Bienvenido a la libreria</h1>")
    

def vacanteeditar(request,id):
    vacante = Vacante.objects.all()
    vacantes = Vacante.objects.get(id=id)
    formulariovc = VacanteForm(request.POST or None, request.FILES or None, instance=vacantes)
    dircontactos = Contactos.objects.filter(Empresa='13').values()
    

    #contactos = ContactosForm(request.POST or None, request.FILES or None)
    archivovacante = DocumentForm(request.POST or None, request.FILES or None)
    archivos = ArchivoVacante.objects.filter(vacante=id)    
    categories = Categoria.objects.all()
        
   



    if formulariovc.is_valid() and request.POST:
        formulariovc.save()
        return redirect('vacantelistar')
        #return HttpResponse("<h1>Bienvenido a la libreria</h1>")

    #codigo para subir y crear archivos de las vacantes
    if 'subirdocumento' in request.POST:
        return HttpResponse("<h1>Bienvenido a la libreria</h1>")
    #fin codigo para subir y crear archivos de las vacantes

    return render(request, 'crud_Vacantes/editar.html', {'formulariovc': formulariovc, 'categories': categories, 'archivos':archivos, 'dircontactos':dircontactos})
    #return render(request, 'index.html')

def vacanteeliminar(request,id):
    vacantes = Vacante.objects.get(id=id)
    vacantes.delete()
    return redirect('vacantelistar')
   
    # ********************************************

from django.views.decorators.clickjacking import xframe_options_exempt
@xframe_options_exempt
def policia(request):
    return render(request, 'crud_Vacantes/policia.html') 

@xframe_options_exempt
def procuraduria(request):
    return render(request, 'crud_Vacantes/procuraduria.html') 

@xframe_options_exempt
def contraloria(request):
    return render(request, 'crud_Vacantes/pcontraloria.html') 

@xframe_options_exempt
def performance(request):
    return render(request, 'crud_Vacantes/performance.html')

def portada(request):
    return render(request, 'Portada.html')
  
def grafica(request):
    return render(request, 'crud_Vacantes/pgrafica.html')  




#https://www.youtube.com/watch?v=Ws7Wy5EHaXY
def addarchivovacante(request):
    vacantes = Vacante.objects.all()
    categories = Categoria.objects.all()
    archivos = ArchivoVacante.objects.all()
    #categories = DocumentForm(request.POST or None, request.FILES or None)

    if 'message_frm' in request.POST:
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Categoria.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Categoria.objects.get_or_create(name=data['category_new'])
            #print (category)
        else:
            category = None
        #print(category)

        for image in images:
            photo = ArchivoVacante.objects.create(
                categoria=category,
                vacante=data['description'],
                archivo=image,
                formularios = data['pruebas_link'],
            )
        return redirect('addarchivovacante')
    context = {
    'categories': categories,
    'archivos':archivos,
    'vacantes':vacantes
    }
    return render(request, 'Crud_Vacantes/archivos.html', context)