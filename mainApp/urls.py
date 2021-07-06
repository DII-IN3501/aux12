from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('', index, name="index"),
    path('pedir/', pedir, name="pedir"),
    path('pedidos/', pedidos, name="pedidos"),
    path('reserva/', reservaView, name="reservaView"),
    path('reservar/', reservar, name="reservar"),
    path('query0/', query0, name="query0"),
    path('query1/', query1, name="query1"),
    path('query2/', query2, name="query2"),
    path('query3/', query3, name="query3"),
    path('query4/', query4, name="query4"),
    path('query5/', query5, name="query5"),
    path('query6/', query6, name="query6"),
]
