from django.db import models

# Create your models here.

class Alojamiento(models.Model):
    state = models.CharField(max_length=30, primary_key=False)
    town = models.CharField(max_length=50, primary_key=False)
    address = models.CharField(max_length=100, primary_key=False)
    #tipo_alojamiento = models.ForeignKey(TipoAlojamiento, on_delete=models.CASCADE)
    type= models.CharField(max_length=30, primary_key=False)
    category = models.CharField(max_length=30, primary_key=False)


