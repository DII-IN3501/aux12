from django.db import models
from userApp.models import Cliente

class Pizza(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True)
    imagen = models.ImageField(upload_to="pizza-img/")

    def __str__(self):
        return "Pizza {}: {} -- {}".format(self.id, self.nombre, self.descripcion)

class Pedido(models.Model):
    fechahora = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return "Pedido N°{} -- {}".format(self.id, fechahora)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=255)
    proveedor = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# Relaciones
class Carrito(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='carritos')
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    tamano = models.CharField(max_length=15, choices=(("M", "Mediana"),
                                                      ("L", "Familiar"),
                                                      ("XL", "XL")))

class IngredientePizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)


# Actualización

class Mesa(models.Model):
    # Consideraremos el id como el número de la mesa
    ubicacion = models.CharField(max_length=15, choices=(("1P", "Primer Piso"),
                                                         ("2P", "Segundo Piso")))

class Reserva(models.Model):
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE, related_name='mesas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='clientes')
    horario = models.DateTimeField()
