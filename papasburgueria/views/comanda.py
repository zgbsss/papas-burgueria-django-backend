from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Comanda
from papasburgueria.serializers import ComandaSerializer, CriarEditarComandaSerializer

class ComandaViewSet(ModelViewSet):
    queryset = Comanda.objects.all()
    serializer_class = ComandaSerializer

    def get_serializer_class(self):
        if self.action == "create" or self.action == "update":
            return CriarEditarComandaSerializer
        return ComandaSerializer

# aula 30, corrigir erro cm create