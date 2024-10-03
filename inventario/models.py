from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Element(models.Model):

    nombre = models.CharField(null=False, blank=False, max_length=100)
    precio_compra = models.IntegerField(null=False, blank=False)  #lo que costo
    precio_venta = models.IntegerField(null=False, blank=False, default=0) #en lo que lo vendo
    cantidad = models.PositiveIntegerField(null=False, blank=False, default=0) #la cantidad que hay
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'elemento'

class Vale_compra(models.Model):

    cantidad_elementos = models.IntegerField(null=False, blank=False)
    inversion_total = models.IntegerField(null=False, blank=False, default=0)
    fecha_compra = models.DateField(default=date.today, blank=False, null=False)

    class Meta:
        db_table = 'lista_compras'

class Compra(models.Model):

    vale = models.ForeignKey(Vale_compra, on_delete=models.CASCADE, db_tablespace='lista_compras')
    cantidad = models.PositiveIntegerField(null=False, blank=False, default=0)
    elemento = models.ForeignKey(Element, on_delete=models.CASCADE, default=1)
    inversion = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.fecha_compra

    class Meta:
        db_table = 'compra_elementos'

class Vale_venta(models.Model):

    cantidad_elementos = models.IntegerField(null=False, blank=False, default=0)
    monto_vendido = models.IntegerField(null=False, blank=False, default=0)
    ganancia_total = models.IntegerField(null=False, blank=False, default=0)
    fecha_venta = models.DateField(default=date.today, blank=False, null=False)

    class Meta:
        db_table = 'lista_ventas'

class Venta(models.Model):

    vale_venta = models.ForeignKey(Vale_venta, on_delete=models.CASCADE, db_tablespace='lista_ventas')
    fecha_venta = models.DateField(default=date.today, blank=False, null=False)
    cantidad = models.PositiveIntegerField(null=False, blank=False, default=0)
    ganancia = models.IntegerField(null=False, blank=False, default=0)
    elemento = models.ForeignKey(Element, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.fecha_venta

    class Meta:
        db_table = 'venta_elementos'


#modelo para representar los reportes de interes
class Operacion(models.Model):

    fecha_operacion = models.DateField(default=date.today, blank=False, null=False)
    operacion = models.CharField(blank=False, null=False)
    cantidad = models.IntegerField(blank=False,null=False, default=0)

    def __str__(self):
        return self.fecha_operacion
    
    class Meta:
        db_table = 'operacion'