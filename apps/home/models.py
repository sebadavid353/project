from django.db import models

# Create your models here.
class producto(models.request):
    titulo =models.CharField(max_length=20)

    def __str__(self):
        return self.titulo
    
class marca(models.request):
    marcas = models.CharField(max_length=30)

    def __str__(self):
        return self.marcas
class modelo(models.request):
    caracteristica = models.CharField(max_length=30)

    def __str__(self):
        return self.caracteristica


