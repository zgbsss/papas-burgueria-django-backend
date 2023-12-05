from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Ingrediente
from papasburgueria.serializers import IngredienteSerializer, IngredienteDetailSerializer

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return IngredienteDetailSerializer
        return IngredienteSerializer