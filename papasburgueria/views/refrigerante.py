from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Refrigerante
from papasburgueria.serializers import RefrigeranteSerializer

class RefrigeranteViewSet(ModelViewSet):
    queryset = Refrigerante.objects.all()
    serializer_class = RefrigeranteSerializer