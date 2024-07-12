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

def gato1(request):
    context={}
    return render(request, 'animales/gato1.html',context)

def perro1(request):
    context={}
    return render(request, 'animales/perro1.html',context)

def formulario(request):
    context={}
    return render(request, 'animales/formulario_adopcion.html',context)



def listar(request):
    producto = Producto.objects.all()
    context = {'productos':producto}
    return render(request, 'animales/crud/listar.html',context)

