from django import forms

class Registro(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput)
    telefono = forms.IntegerField(label='Teléfono')
    direccion = forms.CharField(label='Dirección')

class IniciarSesion(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput)