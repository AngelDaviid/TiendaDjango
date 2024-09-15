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

def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'detalle_producto.html', {'producto': producto})