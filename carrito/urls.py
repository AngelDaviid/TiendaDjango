from django.urls import path
from . import views



urlpatterns = [
    path('agregar/<slug:producto_slug>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<slug:producto_slug>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('', views.ver_carrito, name='ver_carrito'),
    path('actualizar/<slug:producto_slug>/', views.actualizar_cantidad, name='actualizar_cantidad'),
]
