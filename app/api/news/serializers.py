from rest_framework.serializers import ModelSerializer

from app.model import News


class NewsSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_ru', 'description_name_ru', 'type')

    def update(self, instance, validated_data):

        instance.title_name_ru = self.context['request'].data.get('title_name_ru')
        instance.description_name_ru = self.context['request'].data.get('description_name_ru')
        instance.save()
        return instance


class NewsListSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_ru', 'description_name_ru', 'type')
