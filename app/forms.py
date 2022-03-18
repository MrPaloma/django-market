from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm # formulario de registro

class ContactoForm(forms.ModelForm):

    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class" : "form-control"}))

    class Meta:
        model = Contacto
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    fecha_fabricacion = forms.DateField(widget=forms.DateInput(attrs={'class' : 'form-control', 'type' : 'date'}))

    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass
