from django import forms

class ReservaForm(forms.Form):
    horario = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local',
    })
                                  )
    mesa = forms.IntegerField(min_value=1, max_value=3) # Asumimos que existen solo 3 mesas en el local