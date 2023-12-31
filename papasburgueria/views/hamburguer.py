from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Hamburguer
from papasburgueria.serializers import HamburguerSerializer, HamburguerDetailSerializer, HamburguerListSerializer
from rest_framework.permissions import IsAuthenticated

class HamburguerViewSet(ModelViewSet):
    queryset = Hamburguer.objects.all()
    def get_serializer_class(self):
        if self.action == "list":
            return HamburguerListSerializer
        elif self.action == "retrieve":
            return HamburguerDetailSerializer
        return HamburguerSerializer
    
permission_classes = [IsAuthenticated]