from django.urls import path
from .views import agregar_producto, eliminar_producto, home, contacto, galeria, listar_productos, modificar_producto, registro, UploadView, SignedURLView

urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('galeria', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar-producto"),
    path('modificar-producto/<int:id>', modificar_producto, name="modificar-producto"),
    path('eliminar-producto/<int:id>', eliminar_producto, name="eliminar-producto"),
    path('listar-productos/', listar_productos, name="listar-productos"),
    path('registro/', registro, name="registro"),
    path('upload/', UploadView.as_view(), name='upload'),
    path('signed-url/', SignedURLView.as_view(), name='signed-url')
]