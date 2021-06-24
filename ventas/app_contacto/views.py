
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

import random
import csv
from django.contrib import messages
#from django.contrib.messages import constants as messages
from functools import wraps
from urllib.parse import urlparse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.shortcuts import resolve_url
from django.shortcuts import reverse, redirect
from django.utils.http import urlencode
from django import forms

from .forms import  FormularioContacto
from django.core.mail import EmailMessage
#from .models import Actor, Pelicula (sólo si estan creados en el models.py)

# Create your views here.

def contacto(request):
    if request.method =="GET":
        formulario_contacto = FormularioContacto()
        formulario = formulario_contacto
        context = {'formulario':formulario}
        return render(request,'app_contacto/contacto.html', context)
    
    if request.method =='POST':
        formulario_contacto = FormularioContacto(data=request.POST)
        print(formulario_contacto)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde app_Django", 
                    "El isuario con nombre{} con la dirección {} te escribe lo siguiente:\n\n {}".
                    format(nombre,email,contenido),"",["djangopython75@gmail.com"],reply_to=[email])
            
            messages.success(request, f"Información enviada correctamente")

        try:
            email.send()
            return redirect('app_contacto:contacto' )
        except:
            return redirect('app_contacto:contacto' )




