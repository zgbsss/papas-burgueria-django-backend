from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Lucro
from papasburgueria.serializers import LucroSerializer

class LucroViewSet(ModelViewSet):
    queryset = Lucro.objects.all()
    serializer_class = LucroSerializer
