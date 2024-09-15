from django.urls import path
from . import views

app_name = 'categoria'  # Asegúrate de tener esto al inicio

urlpatterns = [
    path('categoria/<slug:slug>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('producto/<int:id>/', views.detalle_producto, name='detalle_producto'),
]
