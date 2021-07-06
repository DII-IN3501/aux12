# Desafío Recuperativo -- Auxiliar 12

## Iniciando proyecto
Para empezar, primero es necesario aplicar las migraciones y poblar la base de datos desde la terminal:
```sh
python manage.py migrate
python manage.py shell < population.py
```

## Realizando las queries
El único archivo a editar es el `mainApp/views.py`. Hay 6 views que deben ser modificados de tal forma que el elemento que se encuentra en el contexto contenga lo que se pide.

### Ejemplo
Si queremos una vista en la cual retorne todas las pizzas disponibles, en la view `query0`:
```python
def query0(request):
    pizzas = Pizza.objects.all()

    context = {"pizzas": pizzas}
    return render(request, 'mainApp/query0.html', context)
```

## Queries (1 pto c/u)
1. [query1] Retornar todos los ingredientes disponibles
2. [query2] Retornar todas las pizzas que contengan más de 3 ingredientes
3. [query3] Retornar todos los pedidos realizados por el cliente «Choro Mota»
4. [query4] Retornar **la cantidad** de pedidos realizados por el usuario de la sesión actual (Esto es, el usuario que se encuentra logeado)
5. [query5] Retornar el pedido con la mayor cantidad de variedad de pizzas (Esto es el pedido con más `Carritos` asociados)
6. [query6] Retornar los clientes con más de 3 pedidos en los últimos 3 meses
