from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Compra
from papasburgueria.serializers import CompraSerializer

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer