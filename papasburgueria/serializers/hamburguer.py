from rest_framework.serializers import ModelSerializer
from papasburgueria.models import Hamburguer

class HamburguerSerializer(ModelSerializer):
    class Meta:
        model = Hamburguer
        fields = "__all__"

class HamburguerDetailSerializer(ModelSerializer):
    class Meta:
        model = Hamburguer
        fields = "__all__"
        depth = 1

class HamburguerListSerializer(ModelSerializer):
    class Meta:
        model = Hamburguer
        fields = ["id", "nome", "preco", "ingredientes", "avaliacao"]