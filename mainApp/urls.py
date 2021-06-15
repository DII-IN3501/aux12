from django.urls import path
from mainApp.views import index, pedir, pedidos

urlpatterns = [
    path('', index, name="index"),
    path('pedir/', pedir, name="pedir"),
    path('pedidos/', pedidos, name="pedidos"),
]
