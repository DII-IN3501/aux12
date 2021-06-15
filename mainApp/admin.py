from django.contrib import admin
from mainApp.models import Pizza, Pedido, Ingrediente, Carrito, IngredientePizza

admin.site.register(Pizza)
admin.site.register(Pedido)
admin.site.register(Ingrediente)
admin.site.register(Carrito)
admin.site.register(IngredientePizza)
