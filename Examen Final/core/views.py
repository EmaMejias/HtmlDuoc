from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Categoria, Producto, Boleta, detalle_boleta
from .forms import ProductoForm, RegistroUserForm, UserEditForm
from core.compras import Carrito
from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Boleta, detalle_boleta



# Create your views here.
def index (request):
    return render(request,'index.html')

def micuenta (request):
    return render(request,'micuenta.html')

def mision_vision (request):
    return render(request,'mision-vision.html')

def proximos_productos (request):
    return render(request,'Proximos_productos_API_priv.html')

def registro_cliente (request):
    return render(request,'registro_cliente.html')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Tu perfil ha sido actualizado!')
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
    
    return render(request, 'registration/profile.html', {
        'user_form': user_form,
    })

@login_required
def crear(request):
    if request.user.is_staff == True:
        if request.method=='POST':
            productoform = ProductoForm(request.POST, request.FILES)
            if productoform.is_valid():
                productoform.save()         #INSERT INTO PRODUCTO
                return redirect ('productos_admin') #...
        else:
            productoform = ProductoForm()
        return render (request, 'crear.html', {'productoform': productoform})
    else:
        return redirect('/')    

@login_required
def detalle(request, id):
    if request.user.is_staff == True:
        producto = get_object_or_404(Producto, idProducto=id) #busqueda de objeto por id
        return render(request, 'detalle.html', {'producto':producto})
    else:
        return redirect('/')

@login_required
def modificar(request, id):
    if request.user.is_staff == True:
        producto = Producto.objects.get(idProducto=id)
        datos ={
            'forModificar': ProductoForm (instance=producto),
            'producto' : producto
        }
        if request.method=='POST':
            formulario = ProductoForm (request.POST,request.FILES,instance=producto)
            if formulario.is_valid():
                formulario.save()
                return redirect('productos_admin')
        return render (request, 'modificar.html',datos)
    else:
        return redirect('/')

@login_required
def eliminar(request, id):
    if request.user.is_staff == True:
        producto = get_object_or_404(Producto, idProducto=id) 
        if request.method=='POST':
            if 'elimina' in request.POST: 
                producto.delete() #eliminamos un obje 
                return redirect('productos_admin') 
        return render(request, 'eliminar.html',{'producto': producto})
    else:
        return redirect('/')

@login_required
def productos_admin (request):
    if request.user.is_staff == True:
        datos = Producto.objects.all()      #select * from Producto
        return render(request,'productos_admin.html', {"datos": datos})
    else:
        return redirect('/')

def cerrar (request):
    logout (request)
    return redirect ('index')

def registrar (request):
    data={
        'form' : RegistroUserForm()
    }
    if request.method == 'POST':
        formulario= RegistroUserForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data["username"],                
                password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect ('index')
        data["form"]=formulario
    return render(request,'registration/registrar.html',data)

#LISTADO PARA USUARIO CLIENTE con busqueda
def productos(request):
    query = request.GET.get('q')
    if query:
        datos = Producto.objects.filter(nombreProducto__icontains=query)
    else:
        datos = Producto.objects.all()
    
    paginator = Paginator(datos, 12)  # Mostrar 10 productos por página

    page = request.GET.get('page')
    try:
        datos = paginator.page(page)
    except PageNotAnInteger:
        # Si la página no es un entero, muestra la primera página.
        datos = paginator.page(1)
    except EmptyPage:
        # Si la página está fuera del rango (por ejemplo, 9999), muestra la última página de resultados.
        datos = paginator.page(paginator.num_pages)
    
    return render(request, 'Productos.html', {"datos": datos})



#METODOS PARA EL CARRITO

def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    producto = get_object_or_404(Producto, idProducto=id)
    try:
        carrito_compra.agregar(producto=producto)
    except ValueError as e:
        messages.error(request, str(e))
    return redirect('productos')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('productos')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('productos')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('productos')

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(idProducto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            producto.stock -= cant
            if producto.stock < 0:
                producto.stock = 0
            producto.save()
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)

#obtener boleta
def obtener_boleta(request):
    if 'boleta' not in request.session:
        return redirect('productos')

    boleta_id = request.session['boleta']
    boleta = Boleta.objects.get(id_boleta=boleta_id)
    detalles = detalle_boleta.objects.filter(id_boleta=boleta)

    
    subtotal = sum([detalle.subtotal for detalle in detalles])
    gastos_envio = round(subtotal * 0.15)
    total_final = subtotal + gastos_envio

    datos = {
        'productos': detalles,
        'fecha': boleta.fechaCompra,
        'subtotal': subtotal,
        'gastos_envio': gastos_envio,
        'total_final': total_final,
        'id_boleta': boleta.id_boleta,
        'estado': 'Procesando pedido',
        'user': request.user  
    }

    return render(request, 'boleta.html', datos)

#PARA HISTORIAL DE COMPRAS
def compras_realizadas(request):
    boletas = Boleta.objects.all().order_by('-fechaCompra')  # Obtener todas las boletas ordenadas por fecha descendente

    datos_compras = []
    for boleta in boletas:
        detalles = detalle_boleta.objects.filter(id_boleta=boleta)
        productos = []
        for detalle in detalles:
            productos.append({
                'nombre': detalle.id_producto.nombreProducto,
                'cantidad': detalle.cantidad,
                'subtotal': detalle.subtotal
            })
        datos_compras.append({
            'boleta': boleta,
            'productos': productos
        })

    return render(request, 'compras_realizadas.html', {'compras': datos_compras})