from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Comanda
from papasburgueria.serializers import ComandaSerializer

class ComandaViewSet(ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer