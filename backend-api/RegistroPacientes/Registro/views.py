from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from .models import *

class PacienteView(APIView):
    serializer_class = PacienteSerializer
    def get_queryset(self):
        pacientes = Paciente.objects.all()
        return pacientes

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            try:
                id = request.query_params["id"]
                if id != None:
                    pacientes = Paciente.objects.get(id=id)
                    serializer = PacienteSerializer(pacientes)
            except:
                pacientes = self.get_queryset()
                serializer = PacienteSerializer(pacientes, many=True)

            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            paciente_data = request.data
            nuevo_paciente = Paciente.objects.create(nombre=paciente_data["nombre"], apellido=paciente_data["apellido"])
            nuevo_paciente.save()

            for numero in paciente_data["numeros"]:
                if Numero_telefonico.objects.filter(numero=numero["numero"]).count() > 0:
                    numero_existente = Numero_telefonico.objects.get(numero=numero["numero"])
                    nuevo_paciente.numeros.add(numero_existente)
                else:
                    nuevo_numero = Numero_telefonico.objects.create(numero=numero["numero"])
                    nuevo_numero.save()
                    nuevo_paciente.numeros.add(nuevo_numero)
            serializer = PacienteSerializer(nuevo_paciente)

            return Response(serializer.data)
    
    def patch(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            data = request.data
            paciente_object = Paciente.objects.get(id=data['id'])

            paciente_object.nombre = data.get("nombre", paciente_object.nombre)
            paciente_object.apellido = data.get("apellido", paciente_object.apellido)
           
            paciente_object.save()
            serializer = PacienteSerializer(paciente_object)

            return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        if request.method == 'DELETE':
            try:
                paciente = Paciente.objects.get(id=request.query_params['id'])
                paciente.delete()
                return Response({'message: Paciente eliminado'})
            except:
                return Response({'message: Error al eliminar el paciente'})

class Numeros_telefonicosViewSet(viewsets.ModelViewSet):
    serializer_class = Numeros_telefonicosSerializer
    def get_queryset(self):
        numeros = Numero_telefonico.objects.all()
        return numeros