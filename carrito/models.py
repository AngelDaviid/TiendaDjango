from django.db import models
from django.contrib.auth.models import User
from myapp.models import Producto

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE,related_name='carrito')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=1)
    
    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    
    def total(self):
        return sum(item.subtotal() for item in self.items.all())
    
    def agregar_producto(self, producto, cantidad=1):
        item, creado = ItemCarrito.objects.get_or_create(carrito = self, producto=producto)
        if creado:
            item.cantidad = cantidad
        else:
            item.cantidad += cantidad
        item.save()
        
    def eliminar_producto(self, producto):
        ItemCarrito.objects.filter(carrito=self, producto=producto).delete()
        
    def vaciar_carrito(self):
        self.items.all().delete()
        
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.cantidad} de {self.producto.nombre} en el carrito"
    
    def subtotal(self):
        return self.producto.precio * self.cantidad