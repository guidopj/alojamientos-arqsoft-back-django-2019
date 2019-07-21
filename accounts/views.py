from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseServerError,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import logging
import json
# Create your views here.

@csrf_exempt
def registerUser(request):
    logger = logging.getLogger(__name__)
    
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        form = UserCreationForm(received_json_data)
        if form.is_valid():
            logger.error("is Valid")
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

def loginUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            login(request,user)
            return HttpResponse(user)
        else:
            return HttpResponseServerError(form.errors)
