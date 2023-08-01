from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Hamburguer
from papasburgueria.serializers import (HamburguerSerializer)

class HamburguerViewSet(ModelViewSet):
    queryset = Hamburguer.objects.all()
    serializer_class = HamburguerSerializer