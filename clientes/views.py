from django.contrib.auth import (authenticate, get_user_model, login,logout)
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserLoginForm
from .models import *
from .forms import *
from proyectovacantes.models import *
from proyectovacantes.forms import *
from .filters import clientefiltro
from django.contrib import messages

#******************configuracion login entrada**********************
#https://www.youtube.com/watch?v=Aqj8no2tb5c
def login_view(request):
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        # HttpResponse("<h1>Bienvenido a la libreria</h1>")
        return render(request, 'index.html',{})
    else:                
        return render(request, 'login.html',{'form':form, 'title':title})

def register_view(request):
    return render(request, 'login.html',{})

def logout_view(request):
    logout(request)
    return render(request, 'login.html',{})

#******************fin configuracion login entrada**********************

#******************CRUD CLIENTES**********************


def clienteslistar(request):
    clientes = Empresa.objects.all()
    filter = clientefiltro(request.GET, queryset=clientes)
    return render(request, 'crud_Clientes/listar.html', {'filter':filter}) 

     
def clientescrear(request):    
    formulario = EmpresaForm(request.POST or None, request.FILES or None)
    formulariosector = SectorForm(request.POST or None, request.FILES or None)
    context={
        'formulario': formulario,
        'formulariosector': formulariosector
    }

    if formulario.is_valid():
        formulario.save()
        return redirect('clienteslistar')

    #actualiza campo del sector economico
    if formulariosector.is_valid() and request.method == 'POST':
        formulariosector.save()
        #return redirect('clienteslistar')

    return render(request, 'crud_Clientes/crear.html', context)
       # HttpResponse("<h1>Bienvenido a la libreria</h1>")

def clienteseditar(request, id):
    vacante = Vacante.objects.all()
    contactos = Contactos.objects.filter(Empresa_id=id)
    clientes = Empresa.objects.get(id=id)
    vacantes = Vacante.objects.filter(Cliente_id=id)
    formulario = EmpresaForm(request.POST or None, request.FILES or None, instance=clientes)
    formulariocontacto = ContactosForm(request.POST or None, request.FILES or None)
    formulariosector = SectorForm(request.POST or None, request.FILES or None)
    archivovacante = DocumentForm(request.POST or None, request.FILES or None)
    formulariovc = VacanteForm(request.POST or None, request.FILES or None)
    ClientesEditarForm = EmpresaEditForm(request.POST or None, request.FILES or None)
    print(clientes.id)

    context={
        'formulario': formulario,
        'formulariosector': formulariosector,
        'contactos': contactos,
        'formulariocontacto': formulariocontacto,
        'formulariovc': formulariovc,
        'vacantes': vacantes,
        'ClientesEditarForm':ClientesEditarForm,
        'archivovacante': archivovacante
    }
        #crear empresa
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('clienteslistar')

        #actualiza campo del sector economico
    if formulariosector.is_valid() and request.method == 'POST':
        formulariosector.save()
        return redirect('clienteslistar')

    #if 'contactoscrear' in request.POST:
    if 'vacantescrear' in request.POST:
        captura = int(id)
        #print(captura)
        Vacante.objects.create(Cliente_id =captura)
        refrescar = '/clienteseditar/'
        #item = str(captura)
        return redirect(refrescar + captura)

    if 'contactocrear' in request.POST:
        captura = int(id)
        #print(captura)
        Contactos.objects.create(Empresa_id =captura)
        refrescar = '/clienteseditar/'
        #item = str(captura)
        return redirect(refrescar + captura)  



    return render(request, 'crud_Clientes/editar.html', context)
    #return render(request, 'index.html')

def clienteseliminar(request,id):
    clientes = Empresa.objects.get(id=id)
    clientes.delete()
    return redirect('clienteslistar')
   
#******************CRUD SECTORES*********************************************

def SectorEconomicocrear(request):
    formulariosector = SectorForm(request.POST or None, request.FILES or None)
    if formulariosector.is_valid():
        formulariosector.save()
        return redirect('clienteslistar')
    return render(request, 'crud_Clientes/modal_sector.html', {'formulariosector': formulariosector})
    
#******************CRUD CONTACTOS**********************

def contactolistar(request):
    contactos = Contactos.objects.all()
    #contactos = Contactos.objects.Get.get(id=1)
    #print(contactos)
    return render(request, 'crud_Contactos/listar.html', {'contactos': contactos}) 
    #return HttpResponse("<h1>Bienvenido a la libreria</h1>")
    

def contactocrear(request):
    formulariocontacto = ContactosForm(request.POST or None, request.FILES or None)
    if formulariocontacto.is_valid():
        formulariocontacto.save()
        return redirect('contactolistar')
    return render(request, 'crud_Contactos/crear.html', {'formulariocontacto': formulariocontacto})
    #return render(request, 'index.html')

def contactoeditar(request, id):
    contactos = Contactos.objects.get(id=id)
    formulariocontacto = ContactosForm(request.POST or None, request.FILES or None, instance=contactos)
    if formulariocontacto.is_valid() and request.POST:
        formulariocontacto.save()
        messages.success(request, 'Actualizado!')
        return redirect('contactolistar')

    return render(request, 'crud_Contactos/editar.html', {'formulariocontacto': formulariocontacto})
    #return render(request, 'index.html')

def contactoeliminar(request,id):
    contactos = Contactos.objects.get(id=id)
    contactos.delete()
    return redirect('contactolistar')

#******************FIN CRUD CONTACTOS**********************