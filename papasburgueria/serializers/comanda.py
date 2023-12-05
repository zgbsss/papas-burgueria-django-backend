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
    class Meta:
        model = Comanda
        fields = ["id", "usuario", "status", "total", "itens"]

class CriarEditarItensComandaSerializer(ModelSerializer):
    class Meta:
        model = ItensComanda
        fields = ["hamburguer", "ingrediente", "bebida", "quantidade"]

class CriarEditarComandaSerializer(ModelSerializer):
    itens = CriarEditarItensComandaSerializer(many=True)
    class Meta:
        model = Comanda
        fields = ["usuario", "itens"]

    def create(self, validated_data):
        itens_data = validated_data.pop("itens")
        comanda = Comanda.objects.create(**validated_data)
        for itens_data in itens_data:
            ItensComanda.objects.create(comanda=comanda, **item_data)
        comanda.save()
        return compra
