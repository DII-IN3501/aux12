from django.urls import path
from mainApp.views import index, pedir, pedidos, reservaView, reservar

urlpatterns = [
    path('', index, name="index"),
    path('pedir/', pedir, name="pedir"),
    path('pedidos/', pedidos, name="pedidos"),
    path('reserva/', reservaView, name="reservaView"),
    path('reservar/', reservar, name="reservar"),
]
