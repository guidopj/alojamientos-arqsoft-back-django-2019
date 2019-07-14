from django.db import models

# Create your models here.

class TypeCode(models.Model):
    type_code = models.CharField(max_length=10, primary_key=False)
    acc_type = models.CharField(max_length=30, primary_key=False)

class Accommodation(models.Model):
    state = models.CharField(max_length=30, primary_key=False)
    town = models.CharField(max_length=50, primary_key=False)
    address = models.CharField(max_length=100, primary_key=False)
    #type_code = models.ForeignKey(TypeCode, on_delete=models.CASCADE)
    type_code = models.CharField(max_length=30, primary_key=False)
    category = models.CharField(max_length=30, primary_key=False)
    


