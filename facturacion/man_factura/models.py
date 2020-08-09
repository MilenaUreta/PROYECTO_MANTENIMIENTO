from django.db import models
from datetime import date

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField(default=0)
    stock = models.IntegerField(default=0)
    iva = models.BooleanField(default=True)

    class Meta:
        verbose_name='producto'
        verbose_name_plural='productos'
    
    def __str__(self):
        return self.descripcion


class Cliente(models.Model):
    ruc = models.CharField(max_length=13,default='9999999999999')
    correo=models.EmailField()
    telefono=models.IntegerField(max_length=10)
    nombre = models.CharField(max_length=300)
    direccion = models.TextField(blank=True,default='S/N', null=True)
    producto = models.ManyToManyField(Producto)

    class Meta:
        verbose_name='cliente'
        verbose_name_plural='clientes'
    
    def __str__(self):
        return self.nombre


class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    fecha = models.DateField(default=date.today())
    total = models.FloatField(default=0)

    class Meta:
        verbose_name='factura'
        verbose_name_plural='facturas'

    def __str__(self):
     return '{},{},{}'.format(self.cliente,self.fecha,self.total)


class DetalleFactura(models.Model):
    factura=models.ForeignKey(Factura, on_delete= models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete= models.CASCADE)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)

    class Meta:
        verbose_name='detalle'
        verbose_name_plural='detalles'
    
    def __str__(self):
     return '{},{},{}'.format(self.factura,self.cantidad,self.subtotal)
