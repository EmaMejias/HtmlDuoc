from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def __str__(self):
       return self.nombre

class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
    nuevo= models.BooleanField()
    marca= models.ForeignKey(Marca, on_delete=models.PROTECT)
    fecha_fabricacion= models.DateField()
    imagen = models.ImageField(upload_to="producto", null=True)

    def __str__(self):
      return self.nombre

class Pintura(models.Model):
    nombre= models.CharField(max_length=50)
    precio= models.IntegerField()
    descripcion= models.TextField()
    fecha_fabricacion= models.DateField()
    imagen = models.ImageField(upload_to="Pintura", null=True)

    def __str__(self):
      return self.nombre

class Escultura(models.Model):
  nombre= models.CharField(max_length=50)
  precio= models.IntegerField()
  descripcion= models.TextField()
  fecha_fabricacion= models.DateField()
  imagen= models.ImageField(upload_to="Escultura", null=True)

  def __str__(self):
    return self.nombre
