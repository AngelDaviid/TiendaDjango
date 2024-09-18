from django.db import models
from categoria.models import Categoria
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    imagen = models.ImageField(upload_to="productos", null=True)
    disponible = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.nombre


#Registro con relaciones 
#Cliente.object.all() mostrar objetos que hay dentro de la tabla
#Cliente.object.Get(id=3) mostrar especificamente
#
