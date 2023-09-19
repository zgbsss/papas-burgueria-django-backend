from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from papasburgueria.models import Comanda, ItensComanda

class ItensComandaSerializer(ModelSerializer):
    total = SerializerMethodField()
    class Meta:
        model = ItensComanda
        fields = ["hamburguer", "quantidade"]
        depth = 2
    def get_total(self, obj):
        return obj.hamburguer.preco * obj.quantidade

class ComandaSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    itens = ItensComandaSerializer(many=True, read_only=True)
    class Meta:
        model = Comanda
        fields = "__all__"