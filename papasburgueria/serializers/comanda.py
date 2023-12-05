from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from papasburgueria.models import Comanda, ItensComanda

class ItensComandaSerializer(ModelSerializer):
    class Meta:
        model = ItensComanda
        fields = ["hamburguer", "ingrediente", "bebida", "quantidade"]
        depth = 2
        total = SerializerMethodField()
    def get_total(self, obj):
        return obj.hamburguer.preco * obj.quantidade

class ComandaSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensComandaSerializer(many=True, read_only=True)
    fields = ("id", "usuario", "status", "total", "itens")
    class Meta:
        model = Comanda
        fields = "__all__"