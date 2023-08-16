from rest_framework.viewsets import ModelViewSet
from papasburgueria.models import Ingrediente
from papasburgueria.serializers import IngredienteSerializer

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
