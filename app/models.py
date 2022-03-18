from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100,verbose_name='nombre')
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion = models.DateTimeField()
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self) -> str:
        return self.nombre

opciones_consultas = [
    [0, "consultas"],
    [1, "reclamo"],
    [2, "sugerencias"],
    [3, "felicitaciones"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre

class Archivo(models.Model):
    created_at = models.DateField(auto_now_add=True)
    nombre = models.CharField(max_length=100)
    archivo = models.ImageField(upload_to="archivos", null=True)