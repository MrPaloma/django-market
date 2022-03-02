from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        'productos' : Producto.objects.all()
    }

    return render(request, 'app/home.html', context)

def contacto(request):
    context = {
        'form' : ContactoForm() # se pasa una instancia
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            context['mensaje'] = "Contacto guardado"
        else:
            context['form'] = formulario

    return render(request, 'app/contacto.html', context)

def galeria(request):
    return render(request, 'app/galeria.html')

def agregar_producto(request):

    context = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        form = ProductoForm(data = request.POST, files = request.FILES)

        if form.is_valid():
            form.save()
            context['mensaje'] = 'PRODUCTO GUARDADO!!'
        else :
            context['form'] = form 

    return render(request, 'app/productos/agregar.html', context)

def listar_productos(request):
    productos = Producto.objects.all()

    context = {
        'productos' : productos
    }

    return render(request, 'app/productos/listar.html', context)

def modificar_producto(request, id):

    producto = get_object_or_404(Producto, id = id)

    context = {
        'form' : ProductoForm(instance = producto)
    }

    if request.method == 'POST':
        form = ProductoForm(data = request.POST, instance = producto, files = request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "PRODUCTO MODIFICADO!!")
            return redirect(to="listar-productos")
        else :
            context['form'] = form 

    return render(request, 'app/productos/modificar.html', context)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id = id)
    producto.delete()
    messages.success(request, "PRODUCTO ELIMINADO!!")

    return redirect(to="listar-productos")