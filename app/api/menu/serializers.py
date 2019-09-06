from rest_framework.serializers import ModelSerializer

from app.model import Menu


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name_ru',)