from django.shortcuts import render

from .carro import Carro
from app_tienda.models import Productos
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('app_tienda:tienda')


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('app_tienda:tienda')

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto=Productos.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('app_tienda:tienda')

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('app_tienda:tienda')

