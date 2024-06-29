from django.shortcuts import render
from django.http import HttpResponse
from .models import Ayuda,Producto


# Create your views here.

def index(request):
    context={}
    return render(request, 'animales/home.html',context)

def auspiciadores(request):
    context={}
    return render (request, 'animales/auspiciadores.html',context)

def apadrinacion(request):
    context={}
    return render (request, 'animales/apadrinacion.html', context)

def adopcionP(request):
    context={}
    return render (request, 'animales/adopcion_perrito.html',context)

def adopcionP2(request):
    context={}
    return render (request, 'animales/adopcion_perrito2.html',context)

def perritoAdulto(request):
    context={}
    return render (request, 'animales/perrito_adulto.html',context)

def perritoCachorro(request):
    context={}
    return render (request, 'animales/perrito_cachorro.html',context)

def adopcionG(request):
    context={}
    return render (request, 'animales/adopcion_gatito.html',context)

def gatitoCachorro(request):
    context={}
    return render (request, 'animales/gatito_cachorro.html',context)

def gatoAdulto(request):
    context={}
    return render(request, 'animales/gato_adulto.html',context)



def orm1(request):
    productos=Producto.objects.all()
    context={"productos":productos}
    return render (request, 'animales/orm1.html',context)

def crud (request):
    productos = Producto.objects.all()
    context = {'productos' : productos}
    return render (request, 'animales/crud_lista.html',context)

