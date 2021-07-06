from django.shortcuts import render
from mainApp.models import Pizza, Ingrediente, Pedido, Carrito, Reserva, Mesa

from mainApp.forms import ReservaForm

def index(request):
    context = {"pizzas": Pizza.objects.all()}
    return render(request, 'mainApp/index.html', context)

def pedir(request):
    pedido = Pedido(cliente=request.user.cliente)
    pedido.save()

    for k in request.POST:
        if k.startswith('pizza-'):
            pizza_id = int(k[6:]) # Extraemos solo el número de pizza-n y lo convertimos a entero. Ej: "pizza-4" -> 4
            cantidad = int(request.POST[k]) # Convertimos a entero esta cantidad
            tamano = request.POST["tamano-"+str(pizza_id)] # Extraemos el tamaño de la pizza por su ID.

            carrito = Carrito(pedido=pedido,
                              pizza=Pizza.objects.get(id=pizza_id),
                              cantidad=cantidad,
                              tamano=tamano)
            carrito.save()

    #context = {"pizzas": Pizza.objects.all()}
    #return render(request, 'mainApp/index.html', context)
    return index(request)

def pedidos(request):
    listapedidos = Pedido.objects.filter(cliente=request.user.cliente)

    context = {"pedidos": listapedidos}
    return render(request, 'mainApp/pedidos.html', context)

# Actualización
def reservaView(request):
    form = ReservaForm()
    return render(request, 'mainApp/reserva.html', {'form': form})

def reservar(request):
    cliente = request.user.cliente
    mesa = request.POST['mesa']
    horario = request.POST['horario']

    reserva = Reserva(cliente=cliente,
                      mesa=Mesa.objects.get(id=int(mesa)),
                      horario=horario)

    reserva.save()

    return index(request)

def query0(request):
    pizzas = Pizza.objects.all()

    context = {"pizzas": pizzas}
    return render(request, 'mainApp/query0.html', context)

def query1(request):
    ingredientes = []

    context = {"ingredientes": ingredientes}
    return render(request, 'mainApp/query1.html', context)

def query2(request):
    pizzas = []

    context = {"pizzas": pizzas}
    return render(request, 'mainApp/query2.html', context)

def query3(request):
    pedidos = []

    context = {"pedidos": pedidos}
    return render(request, 'mainApp/query3.html', context)

def query4(request):
    cantidad_pedidos = 0

    context = {"cantidad_pedidos": cantidad_pedidos}
    return render(request, 'mainApp/query4.html', context)

def query5(request):
    pedido = None

    context = {"pedido": pedido}
    return render(request, 'mainApp/query5.html', context)

def query6(request):
    clientes = []

    context = {"clientes": clientes}
    return render(request, 'mainApp/query6.html', context)
