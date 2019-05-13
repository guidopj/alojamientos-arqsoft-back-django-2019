from django.shortcuts import render
from .forms import AlojamientoForm
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.

def crearAlojamiento(request):
    if request.method == 'POST':
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.save()
            messages.success(request, "Alojamiento creado correctamente")
            return redirect('')
        else:
            context = {'errors': form.errors}
            return render(request, '', context)
