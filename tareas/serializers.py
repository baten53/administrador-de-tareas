from rest_framework import serializers
from tareas.models import Usuario, Estado, Tarea


class TareasuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        

class TareaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class TareastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'        

