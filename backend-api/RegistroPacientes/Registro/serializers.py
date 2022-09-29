from rest_framework import serializers
from .models import *

class Numeros_telefonicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numero_telefonico
        fields = ('numero', 'activo')

class PacienteSerializer(serializers.ModelSerializer):
    numeros = Numeros_telefonicosSerializer(read_only=False, many=True)
    class Meta:
        model = Paciente
        fields = ('id','nombre', 'apellido', 'numeros')