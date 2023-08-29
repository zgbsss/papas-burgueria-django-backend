from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Bebida
from papasburgueria.serializers import BebidaSerializer

class BebidaViewSet(ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer
# 