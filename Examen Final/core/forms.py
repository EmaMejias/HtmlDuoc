from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Categoria, Producto



class RegistroUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name', 'last_name','email','password1', 'password2']

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields=['idProducto', 'nombreProducto', 'descripcionProducto', 'precio', 'stock', 'categoria', 'imagen']
        labels= {
            'idProducto': 'ID producto',
            'nombreProducto': 'Nombre',
            'descripcionProducto':'Descripción',
            'precio': 'Precio',
            'stock': 'Stock',
            'categoria': 'Categoria',
            'imagen': 'Imagen'
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID producto',
                    'id': 'idproducto'
                }
            ),
            'nombreProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto',
                    'id': 'nombre'
                }
            ),
             'descripcionProducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripción del producto',
                    'id': 'descripcionProducto'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto',
                    'id': 'precio'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el stock del producto',
                    'id': 'stock'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            )




        }