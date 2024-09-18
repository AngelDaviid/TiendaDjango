from django.shortcuts import render, get_object_or_404
from .models import Categoria
from myapp.models import Producto

# Create your views here.

def categorias(request):
    categorias = Categoria.objects.all()
    return{'categorias': categorias}

def categoria_detalles(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    return render(request, 'categoria/categoria_detalles.html', {'categoria': categoria})

def productos_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    productos = Producto.objects.filter(categoria=categoria)
    context={
        'categoria': categoria,
        'productos': productos
    }
    return render(request, 'productos_por_categoria.html', context)

def producto_detail(request, producto_slug):
    producto = get_object_or_404(Producto, slug=producto_slug)
    return render(request, 'producto_detail.html', {'producto': producto})