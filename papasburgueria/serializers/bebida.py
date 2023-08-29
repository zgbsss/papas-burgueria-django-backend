from rest_framework.serializers import ModelSerializer
from papasburgueria.models import Bebida

class BebidaSerializer(ModelSerializer):
    class Meta:
        model = Bebida
        fields = "__all__"