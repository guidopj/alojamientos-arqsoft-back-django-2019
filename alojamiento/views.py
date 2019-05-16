from .forms import AlojamientoForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)
import json

# Create your views here.
@csrf_exempt
def crearAlojamiento(request):

    if request.method == 'POST':
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        form = AlojamientoForm(received_json_data)
        if form.is_valid():
            alojamiento = form.save(commit=False)
            alojamiento.save()
            return HttpResponse("Alojamiento creado correctamente")
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR: " + str(context))
