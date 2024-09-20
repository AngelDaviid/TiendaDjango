from django.contrib import admin
from myapp.models import Producto
from clientes.models import Cliente
from Pedidos.models import Pedido, ItemPedido
from categoria.models import Categoria
from carrito.models import Carrito
from carrito.models import ItemCarrito



admin.site.register(Cliente)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
admin.site.register(ItemPedido)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Pedido)

# Register your models here.
