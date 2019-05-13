from django.db import models

# Create your models here.

class Alojamiento(models.Model):
    provincia = models.CharField(max_length=30, primary_key=False)
    localidad = models.CharField(max_length=30, primary_key=False)
    direccion = models.CharField(max_length=100, primary_key=False)
    #tipo_alojamiento = models.ForeignKey(TipoAlojamiento, on_delete=models.CASCADE)
    tipo_alojamiento = models.CharField(max_length=30, primary_key=False)
    cant_estrellas = models.IntegerField(default=0)


