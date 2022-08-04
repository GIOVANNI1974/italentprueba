import django_filters
from django_filters import rest_framework as filters
from .models import *

class clientefiltro(django_filters.FilterSet):
    class Meta:
        model = Empresa
        fields = {
            'id':['icontains'], 
            'RazonSocial': ['icontains']

        }
