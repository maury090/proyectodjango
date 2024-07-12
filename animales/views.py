from django.shortcuts import render, redirect
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

def agregar_producto(request):
    if request.method == 'POST':
        id_producto = request.POST['idProducto']
        nombre_producto = request.POST['nombreProducto']
        marca_producto = request.POST['marcaProducto']
        valor_producto = request.POST['precio']
        id_ayuda = request.POST['tipo_producto']
        imagen = request.FILES['imagen']  # Para manejar la imagen cargada

        ayuda = Ayuda.objects.get(id_ayuda=id_ayuda)
        
        producto = Producto(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            marca_producto=marca_producto,
            valor_producto=valor_producto,
            id_ayuda=ayuda,
            imagen=imagen  # Asegúrate de tener un campo de imagen en tu modelo
        )
        
        producto.save()

        return redirect('listar')
    
    ayudas = Ayuda.objects.all()
    return render(request, 'animales/crud/agregar.html', {'ayudas': ayudas})





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
    



def agregar_producto(request):
    if request.method == 'POST':
        id_producto = request.POST['idProducto']
        nombre_producto = request.POST['nombreProducto']
        marca_producto = request.POST['marcaProducto']
        valor_producto = request.POST['precio']
        id_ayuda = request.POST['tipo_producto']
        imagen = request.FILES['imagen']  # Para manejar la imagen cargada

        ayuda = Ayuda.objects.get(id_ayuda=id_ayuda)
        
        producto = Producto(
            id_producto=id_producto,
            nombre_producto=nombre_producto,
            marca_producto=marca_producto,
            valor_producto=valor_producto,
            id_ayuda=ayuda,
            imagen=imagen  # Asegúrate de tener un campo de imagen en tu modelo
        )
        
        producto.save()

        return redirect('listar')
    
    ayudas = Ayuda.objects.all()
    return render(request, 'animales/crud/agregar.html', {'ayudas': ayudas})
    
