#from attr import fields
from django import forms
from .models import *
from clientes.models import Contactos
from proyectovacantes.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column, HTML, Div
from crispy_forms.bootstrap import Tab, TabHolder, InlineField

#from candidatos.models import Candidato


#https://www.youtube.com/watch?v=I2-JYxnSiB0 (corrige el problema de fechas edit)
class DateInput(forms.DateInput):
    input_type = 'date'

#https://blog.bixly.com/awesome-forms-django-crispy-forms
#https://simpleisbetterthancomplex.com/tutorial/2018/11/28/advanced-form-rendering-with-django-crispy-forms.html
#https://dev.to/djangotricks/guest-post-django-crispy-forms-advanced-usage-example-51m0


class VacanteCrearForm(forms.ModelForm):
    class Meta:
        model =  Vacante
        fields = ['Cliente']
        #fields = '__all__'



class VacanteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        


    class Meta:
        model =  Vacante
        fields = '__all__'
        widgets = {
            'Cliente': forms.Select(attrs={'class':'form-select', 'placeholder':'Cliente'}),
            'contacto': forms.Select(attrs={'class':'form-select'}),
            'Depto': forms.Select(attrs={'class':'form-select'}),
            'Ciudad': forms.Select(attrs={'class':'form-select'}),
            'Sector': forms.Select(attrs={'class':'form-select'}),
            'Genero': forms.Select(attrs={'class':'form-select'}),
            'Educacion': forms.Select(attrs={'class':'form-select'}),
            'Especializacion': forms.Select(attrs={'class':'form-select'}),
            'Presencialidad': forms.Select(attrs={'class':'form-select'}),
            'TipoContrato': forms.Select(attrs={'class':'form-select'}),
            'Entrevista': forms.Select(attrs={'class':'form-select'}),    
            'EstadoDDR': forms.Select(attrs={'class':'form-select'}),
            'ConocimientoEspecifico': forms.Textarea(attrs={'class':'form-control', 'rows':"3" }),
            'NotaEspecial': forms.Textarea(attrs={'class':'form-control', 'rows':"6" }),
           # 'Salario': forms.Textarea(attrs={'class':'form-control'}),
           
           # 'FechaInicio': forms.DateInput(attrs={'type':DateInput()}),
           # 'FechaFin': forms.DateInput(attrs={'type': DateInput()})   
            
            }
      
        

class DocumentForm(forms.ModelForm):
    class Meta:
        model = ArchivoVacante
        fields = '__all__'
        #fields = ('description', 'document', )


class ContactosForm(forms.ModelForm):
    class Meta:
        model = Contactos
        fields = '__all__'
        widgets = {
            'contacto': forms.Select(attrs={'class':'form-select', 'placeholder':'Contacto'}),
        }


