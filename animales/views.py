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
    productos = Producto.objects.all()
    context = {'productos':productos}
    return render(request, 'animales/crud/listar.html',context)

def agregar(request):
    if request.method is not "POST":
        ayudas = Ayuda.objects.all()
        context={'ayudas':ayudas}
        return render(request, 'animales/crud/agregar.html',context)
    
    else:
        id_producto = request.POST["idProducto"]
        nombre_producto = request.POST["nombreProducto"]
        marca_producto = request.POST["marcaProducto"] 
        precio_producto = request.POST["precio"]
        ayuda = request.POST["tipo_producto"]
        imagen = request.POST["imagen"]


        objAyuda=Ayuda.objects.get(id_ayuda = ayuda)
        obj=Producto.objects.create ( id_producto = id_producto,
                                     nombre_producto = nombre_producto,
                                     marca_producto = marca_producto,
                                     precio_producto = precio_producto,
                                     id_ayuda = objAyuda,
                                     imagen = imagen)
        obj.save()
        context={'mensaje': "Datos guardados"}
        return render(request, 'animales/crud/agregar.html',context)

def eliminar(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto = pk)

        producto.delete()
        mensaje="Producto eliminado"
        productos = Producto.objects.all()
        context = {'productos': productos, 'mensaje':mensaje}
        return render(request, 'animales/crud/listar.html',context)
    
    except:
        mensaje = "Error, producto no existe"
        productos = Producto.objects.all()
        context = {'productos':productos, 'mensaje':mensaje}
        return render (request, 'animales/crud/listar.html',context)
    
