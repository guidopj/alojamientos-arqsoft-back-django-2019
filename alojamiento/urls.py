from django.urls import path
from . import views

urlpatterns = [
    path('crearAlojamiento', views.crearAlojamiento, name="crearAlojamiento")
]