from rest_framework.serializers import ModelSerializer

from app.model import Forms


class ReformSerializer(ModelSerializer):
    class Meta:
        model = Forms
        fields = ('title_name_ru', 'description_name_ru', 'image')

    def update(self, instance, validated_data):

        instance.title_name_ru = self.context['request'].data.get('title_name_ru')
        instance.description_name_ru = self.context['request'].data.get('description_name_ru')
        instance.image = self.context['request'].data.get('image')

        instance.save()
        return instance


class ReformCreateSerializer(ModelSerializer):
    class Meta:
        model = Forms
        fields = ('title_name_ru', 'description_name_ru', 'image', 'type')



class ReformListSerializer(ModelSerializer):
    class Meta:
        model = Forms
        fields = ('title_name_ru', 'description_name_ru','image',  'type')
