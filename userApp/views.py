from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from userApp.models import Cliente

from userApp.forms import IniciarSesion, Registro

def registerView(request):
    form = Registro()
    return render(request, 'userApp/register.html', {'form': form})

def newuser(request):
    username = request.POST['username']
    password = request.POST['password']
    telefono = request.POST['telefono']
    direccion = request.POST['direccion']
    user = User.objects.create_user(username=username, password=password)

    cliente = Cliente(user=user, telefono=telefono, direccion=direccion)
    cliente.save()

    return render(request, 'mainApp/index.html')

def loginView(request):
    form = IniciarSesion()
    return render(request, 'userApp/login.html', {'form': form})

def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    usuario = authenticate(username=username, password=password)
    login(request, usuario)
    return render(request, 'mainApp/index.html')

def logoutView(request):
    logout(request)
    return render(request, 'mainApp/index.html')