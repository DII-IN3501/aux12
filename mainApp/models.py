from django.db import models
from userApp.models import Cliente

class Pizza(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to="pizza-img/")

class Pedido(models.Model):
    fechahora = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=255)
    proveedor = models.CharField(max_length=255)

# Relaciones
class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    tamano = models.CharField(max_length=15, choices=(("M", "Mediana"),
                                       ("L", "Familiar"),
                                       ("XL", "XL")))

class IngredientePizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)