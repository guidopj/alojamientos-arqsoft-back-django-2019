from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.http import HttpResponseServerError,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #username = form.cleaned_data['username']
            form.save(commit=False)
            #messages.success(request, f'Usuario {username} creado correctamente')
            return HttpResponse("Usuario creado correctamente")
        else:
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
