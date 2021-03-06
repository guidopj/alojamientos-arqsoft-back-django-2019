from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseServerError,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import logging
import json

logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def registerUser(request):
    
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        form = UserCreationForm(received_json_data)
        if form.is_valid():
            username = form.cleaned_data['username']
            #email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username)
            user.set_password(password)
            user.save()
            #messages.success(request, f'Usuario {username} creado correctamente')
            return HttpResponse("Usuario creado correctamente")
        else:
            logger.error(form.errors)
            return HttpResponseServerError(form.errors)
    else:
        return HttpResponse("nada")

@csrf_exempt
def loginUser(request):
    data = request.body.decode('utf-8')
    received_json_data = json.loads(data)
    if request.method == 'POST':
        username = received_json_data['username']
        password = received_json_data['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse(user)
        else:
            return HttpResponseServerError("Credentials didnt matched")
    else:
        return HttpResponseServerError("method not allowed")
