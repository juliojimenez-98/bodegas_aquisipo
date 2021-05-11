from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50)
    descripcion_producto = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_producto
    