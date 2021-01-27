from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Lacteos(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre
    


class Producto(models.Model):
    nombre  = models.CharField(max_length= 100)
    fecha_elaboracion = models.IntegerField()
    fecha_caducidad = models.IntegerField()
    tipo = models.ForeignKey(Lacteos, on_delete=CASCADE)

    def __str__(self):
        return self.nombre
    
