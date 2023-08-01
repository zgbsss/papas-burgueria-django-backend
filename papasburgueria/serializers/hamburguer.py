from rest_framework.serializers import ModelSerializer
from papasburgueria.models import Hamburguer

class HamburguerSerializer(ModelSerializer):
    class Meta:
        model = Hamburguer
        fields = "__all__"