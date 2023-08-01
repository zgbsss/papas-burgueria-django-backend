from rest_framework.serializers import ModelSerializer
from papasburgueria.models import Lucro

class LucroSerializer(ModelSerializer):
    class Meta:
        model = Lucro
        fields = "__all__"