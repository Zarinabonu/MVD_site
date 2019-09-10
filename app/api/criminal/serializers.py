from rest_framework.serializers import ModelSerializer

from app.model import Criminal

from app.model import Static_criminal, Criminal_type, Region


class Static_criminalSerialzier(ModelSerializer):
    class Meta:
        model = Static_criminal
        fields = ('region', 'criminal_type', 'count')


class CriminalSerializer(ModelSerializer):
    class Meta:
        model = Criminal
        fields = ('description_name_ru', 'image')

    def update(self, instance, validated_data):

        instance.description_name_ru = self.context['request'].data.get('description_name_ru')
        instance.image = self.context['request'].data.get('image')

        instance.save()
        return instance


class CriminalListSerializer(ModelSerializer):
    class Meta:
        model = Criminal
        fields = ('description_name_ru', 'image')
