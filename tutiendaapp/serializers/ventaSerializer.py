from rest_framework import serializers
from tutiendaapp.models import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id','Hora','Fecha']