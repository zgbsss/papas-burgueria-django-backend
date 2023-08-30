from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from papasburgueria.models import Compra, ItensCompra

class ItensCompraSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItensCompra
        fields = ["hamburguer", "quantidade"]
        depth = 2
    def get_total(self, obj):
        return obj.hamburguer.preco * obj.quantidade

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensCompraSerializer(many=True, read_only=True)
    class Meta:
        model = Compra
        fields = "__all__"