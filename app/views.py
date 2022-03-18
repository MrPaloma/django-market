import boto3
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Archivo, Producto
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login # permite autenticar al usuario
from django.core.paginator import Paginator
from django.conf import settings
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse
from .models import UploadFile
import json

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
            messages.success(request, "PRODUCTO GUARDADO!!")
        else :
            context['form'] = form 

    return render(request, 'app/productos/agregar.html', context)

def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404

    context = {
        'entity' : productos,
        'paginator' : paginator
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

def registro(request):
    context = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST' :
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Te has registrado correctamente')
            return redirect(to="home")
        context['form'] = formulario

    return render(request, 'registration/registro.html', context)

class SignedURLView(generic.View):
    def post(self, request, *args, **kwargs):
        session = boto3.session.Session()
        client = session.client(
            "s3",
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        url = client.generate_presigned_url(
            ClientMethod="put_object",
            Params={
                "Bucket": settings.AWS_STORAGE_BUCKET_NAME,
                "Key": f"archivos/{json.loads(request.body)['fileName']}",
            },
            ExpiresIn=300,
        )
        return JsonResponse({"url": url})

class UploadView(generic.CreateView):
    template_name = "upload.html"
    model = Archivo
    fields = ['file']

    def get_success_url(self):
        return reverse("upload")
    
    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        context.update({
            "uploads": Archivo.objects.all()
        })
        return context