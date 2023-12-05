from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Bebida
from papasburgueria.serializers import BebidaSerializer, BebidaDetailSerializer

class BebidaViewSet(ModelViewSet):
    queryset = Bebida.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return BebidaDetailSerializer
        return BebidaSerializer