from django.db import models
from django.core.validators import MinValueValidator

from datetime import date
from django.utils import timezone

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    # https://docs.djangoproject.com/en/5.1/ref/validators/#minvaluevalidator
    fecha_fabricacion = models.DateField(validators=[MinValueValidator(limit_value=date(2015, 1, 1))])
    # fecha_fabricacion = models.DateTimeField(validators=[MinValueValidator(limit_value=timezone.make_aware(datetime(2015, 1, 1)))])
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.nombre
