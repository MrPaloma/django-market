from django.urls import path
from .views import agregar_producto, eliminar_producto, home, contacto, galeria, listar_productos, modificar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('galeria', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar-producto"),
    path('modificar-producto/<int:id>', modificar_producto, name="modificar-producto"),
    path('eliminar-producto/<int:id>', eliminar_producto, name="eliminar-producto"),
    path('listar-productos/', listar_productos, name="listar-productos"),
]