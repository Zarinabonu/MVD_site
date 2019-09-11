from rest_framework.serializers import ModelSerializer

from app.model import International_busines


class InternationalSerializer(ModelSerializer):
    class Meta:
        model = International_busines
        fields = ('title_ru', 'description_ru', 'image')

    def update(self, instance, validated_data):

        instance.title_ru = self.context['request'].data.get('title_ru')
        instance.description_ru = self.context['request'].data.get('description_ru')
        instance.image = self.context['request'].data.get('image')

        instance.save()
        return instance
