from rest_framework import serializers
from tutiendaapp.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'Nombre', 'Precio']