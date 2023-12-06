from rest_framework.serializers import ModelSerializer, SlugRelatedField
from papasburgueria.models import Hamburguer
from uploader.serializers import ImageSerializer
from uploader.models import Image

class HamburguerSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Hamburguer
        fields = "__all__"

class HamburguerDetailSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False)
    class Meta:
        model = Hamburguer
        fields = "__all__"
        depth = 1

class HamburguerListSerializer(ModelSerializer):
    imagem = ImageSerializer(required=False)
    class Meta:
        model = Hamburguer
        fields = ["id", "imagem", "nome", "preco", "ingredientes", "avaliacao"]
        depth = 1