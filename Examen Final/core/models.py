from django.db import models
from distutils.command.upload import upload
import datetime

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='ID de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre categoria')


    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto = models.CharField(primary_key=True, max_length=10, verbose_name='id de producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre del producto')
    descripcionProducto = models.CharField(max_length=300, verbose_name='Descripción del Producto')
    precio = models.IntegerField(blank=True, null=True, verbose_name='Precio')
    stock = models.IntegerField(verbose_name='stock')
    categoria = models.ForeignKey('Categoria', default=1, on_delete=models.CASCADE, verbose_name='Categoria')
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen')

    def __str__(self):
        return self.idProducto
    
class DetallePedido(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)

    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)    

