from django.shortcuts import get_object_or_404, redirect, render
from myapp.models import Producto
from .models import Carrito, ItemCarrito
from django.contrib.auth.decorators import login_required



@login_required
def agregar_al_carrito(request, producto_slug):
    producto = get_object_or_404(Producto, slug=producto_slug)  # Busca el producto por slug
    carrito_item, created = Carrito.objects.get_or_create(usuario=request.user, producto=producto)

    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()

    return redirect('ver_carrito')  # Redirige al carrito después de agregar

def eliminar_del_carrito(request, slug):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if carrito:
        producto = get_object_or_404(Producto, slug=slug)
        carrito.eliminar_producto(producto)
    return redirect('carrito:ver_carrito')

@login_required
def actualizar_cantidad(request, slug):
    carrito = Carrito.objects.filter(usuario=request.user).first()
    if request.method == 'POST' and carrito:
        nueva_cantidad = int(request.POST.get('cantidad', 1))
        item = carrito.items.filter(producto__slug=slug).first()
        if item:
            item.cantidad = nueva_cantidad
            item.save()
    return redirect('carrito:ver_carrito')

@login_required
def ver_carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in carrito_items)
    
    return render(request, 'Carrito.html', {'carrito_items': carrito_items, 'total': total})
