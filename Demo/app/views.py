from django.shortcuts import render
from.models import Producto

# Create your views here.

def home(request):
    producto= Producto.objects.all()
    data= {
        'producto': producto
    }
    return render(request, 'app/home.html', data)
    

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')
