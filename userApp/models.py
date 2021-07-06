from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.IntegerField(null=True)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        "{}: {} {}".format(self.user.username, self.user.first_name, self.user.last_name)
