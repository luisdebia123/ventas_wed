from django.db import models

# Create your models here.

class Categoria_Prod(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ='categoria_producto'
        verbose_name_plural ='categoria_productos'

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(Categoria_Prod, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos', null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name ='producto'
        verbose_name_plural ='productos'

    def __str__(self):
        return self.nombre