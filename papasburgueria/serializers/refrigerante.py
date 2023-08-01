from rest_framework.serializers import ModelSerializer
from papasburgueria.models import Refrigerante

class RefrigeranteSerializer(ModelSerializer):
    class Meta:
        model = Refrigerante
        fields = "__all__"