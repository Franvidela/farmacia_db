from django.shortcuts import render
from .models import Producto

# Create your views here.
Producto.objects.order_by('nombre').values('nombre', 'laboratorio')
