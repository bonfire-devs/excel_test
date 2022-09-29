from email.policy import default
from mailbox import NoSuchMailboxError
from pyexpat import model
from django.db import models

class Numero_telefonico(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.numero)

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numeros = models.ManyToManyField(Numero_telefonico)

    def __str__(self):
        return self.nombre + " " + self.apellido