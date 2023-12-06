from rest_framework.serializers import ModelSerializer, SlugRelatedField
from papasburgueria.models import Ingrediente
from uploader.models import Image
from uploader.serializers import ImageSerializer

class IngredienteSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    class Meta:
        model = Ingrediente
        fields = "__all__"

class IngredienteDetailSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False)
    class Meta:
        model = Ingrediente
        fields = "__all__"
        depth = 1