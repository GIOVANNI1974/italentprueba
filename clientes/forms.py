from django import forms
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .models import *
from proyectovacantes.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, Div
from crispy_forms.bootstrap import Tab, TabHolder, InlineField

#********************configuracion del login*******************
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
      
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Este usuario no existe")
            if not user.check_password(password):
                raise forms.ValidationError("Password Incorrecto")
            if not user.is_active:
                raise forms.ValidationError("Este usuario esta inactivo")
        return super(UserLoginForm, self).clean(*args, **kwargs)

#********************fin configuracion del login*******************

#********************configuracion formularios de Clientes y contactos*******************
class EmpresaForm(forms.ModelForm):
    class Meta:
        model =  Empresa
        #fields = ['nit', 'dv', 'RazonSocial', 'Actividad','Direccion','Pais','Depto','Ciudad','telefonos','email']
        fields = '__all__'


class SectorForm(forms.ModelForm):
    class Meta:
        model =  SectorEconomico
        #fields = ['nit', 'dv', 'RazonSocial', 'Actividad','Direccion','Pais','Depto','Ciudad','telefonos','email']
        fields = '__all__'

class ContactosForm(forms.ModelForm):
    
    class Meta:
        model =  Contactos
        fields = '__all__'
        #fields = ['Pais']
        widgets = {
            'Empresa': forms.Select(attrs={'class':'form-select', 'placeholder':'Empresa'}),
            'Pais': forms.Select(attrs={'class':'form-select', 'placeholder':'Pais'}),
            'Depto': forms.Select(attrs={'class':'form-select', 'placeholder':'Depto'}),
            'Ciudad': forms.Select(attrs={'class':'form-select', 'placeholder':'Ciudad'}),       
            }
   



      


class EmpresaEditForm(forms.ModelForm):

    class Meta:
        model =  Vacante
        fields = '__all__'
        widgets = {
            'Cliente': forms.Select(attrs={'class':'form-select', 'placeholder':'Cliente'}),
            'contacto': forms.Select(attrs={'class':'form-select'}),
            'Depto': forms.Select(attrs={'class':'form-select'}),
            'Ciudad': forms.Select(attrs={'class':'form-select'}),
            'Sector': forms.Select(attrs={'class':'form-select'}),
        
            }
      
        

