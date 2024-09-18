from django.urls import path
from . import views

urlpatterns =[
    path('', views.Home, name='Home'),
    path('services/', views.services),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('carrito/', views.carrito, name='carrito'),
    path('producto/<slug:producto_slug>/', views.producto_detail, name='productos_detalles'),

]