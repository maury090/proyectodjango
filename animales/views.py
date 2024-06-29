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

def crud_agregar(request):
    if request.method is not "POST":
        ayudas=Ayuda.objects.all()
        context={'ayudas':ayudas}
        return render(request, 'animales/crud_agregar.html',context)
    
    else: 
        id_producto=request.POST["idProducto"]
        nombre_producto=request.POST["nombreProducto"]
        marca_producto=request.POST["marcaProducto"]
        valor_producto=request.POST["valorProducto"]
        ayuda=request.POST["ayudaProducto"]

        objAyuda=Ayuda.objects.get(id_ayuda=ayuda)
        obj=Producto.objects.create( id_producto=id_producto,
                                     nombre_producto=nombre_producto,
                                     marca_producto=marca_producto,
                                     valor_producto=valor_producto,
                                     id_ayuda=objAyuda)
        obj.save()
        context={'mensaje':"Datos guardados correctamente"}
        return render (request, 'animales/crud_agregar.html',context)
    

def crud_del(request,pk):
    context={}
    try:
        producto=Producto.objects.get(id_producto=pk)

        producto.delete()
        mensaje= "datos eliminados"
        productos = Producto.objects.all()
        context ={'productos':productos,'mensaje':mensaje}
        return render(request,'animales/crud_lista.html',context)
    
    except: 
        mensaje="id no existe"
        productos = Producto.objects.all()
        context ={'productos':productos,'mensaje':mensaje}
        return render(request, 'animales/crud_lista.html',context)
    

def crud_edit(request,pk):
    if pk != "":
        producto=Producto.objects.get(rut=pk)
        ayudas=Ayuda.objects.all()

        print(type(producto.id_ayuda.ayuda))

        context ={'producto':producto,'ayudas':ayudas}
        if producto:
            return render(request,'animales/crud_edit.html',context)
        else:
            context={'mensaje': "error, id no existe"}
            return render(request,'animales/crud_lista.html',context)
        
def crud_update(request):
    if request.method == "POST":
        id_producto=request.POST["idProducto"]
        nombre_producto=request.POST["nombreProducto"]
        marca_producto=request.POST["marcaProducto"]
        valor_producto=request.POST["valorProducto"]
        ayuda=request.POST["ayuda"]

        objAyuda=Ayuda.objects.get(id_ayuda=ayuda)

        producto = Producto()
        producto.id_producto=id_producto
        producto.nombre_producto=nombre_producto
        producto.marca_producto=marca_producto
        producto.valor_producto=valor_producto
        producto.id_ayuda=objAyuda
        producto.save()

        ayudas=Ayuda.objects.all()
        context={'mensaje': "datos actualizados",'ayudas':ayudas,'producto':producto}
        return render (request,'animales/crud_edit.html',context)
    else:
        productos=Producto.objects.all()
        context={'productos':productos}
        return render (request, 'animales/crud_lista.html',context)
    
    