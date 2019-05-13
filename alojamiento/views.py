from .forms import AlojamientoForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

# Create your views here.
@csrf_exempt
def crearAlojamiento(request):
    if request.method == 'POST':
        form = AlojamientoForm(request.POST)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.save()
            messages.success(request, "Alojamiento creado correctamente")
            return HttpResponse("Alojamiento creado correctamente")
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR")
