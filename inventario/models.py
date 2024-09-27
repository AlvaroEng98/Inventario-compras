from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Element(models.Model):

    nombre = models.CharField(null=False, blank=False, max_length=100)
    precio_compra = models.FloatField(null=False, blank=False)  #lo que costo
    precio_venta = models.FloatField(null=False, blank=False, default=0) #en lo que lo vendo
    cantidad = models.PositiveIntegerField(null=False, blank=False, default=0) #la cantidad que hay
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'elemento'


class Compra(models.Model):

    fecha_compra = models.DateField(default=date.today, blank=False, null=False)
    cantidad = models.FloatField(null=False, blank=False, default=0)
    elemento = models.ForeignKey(Element, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.fecha_compra

    class Meta:
        db_table = 'compra_elementos'

class Venta(models.Model):

    fecha_venta = models.DateField(default=date.today, blank=False, null=False)
    cantidad = models.FloatField(null=False, blank=False, default=0)
    ganancia = models.FloatField(null=False, blank=False, default=0)
    elemento = models.ManyToManyField(Element)

    def __str__(self):
        return self.fecha_venta

    class Meta:
        db_table = 'venta_elementos'


#modelo para representar los reportes de interes