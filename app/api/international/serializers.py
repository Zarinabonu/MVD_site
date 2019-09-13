from rest_framework.serializers import ModelSerializer

from app.model import International_busines


class InternationalSerializer(ModelSerializer):
    class Meta:
        model = International_busines
        fields = ('title_name_ru',
                  'title_name_uz',
                  'full_content_uz',
                  'full_content_ru',
                  'short_content_ru',
                  'short_content_uz',
                  'image')


    def update(self, instance, validated_data):
        instance.title_name_ru = self.context['request'].data.get('title_name_ru')
        instance.title_name_uz = self.context['request'].data.get('title_name_uz')
        instance.full_content_uz = self.context['request'].data.get('full_content_uz')
        instance.full_content_ru = self.context['request'].data.get('full_content_ru')
        instance.short_content_ru = self.context['request'].data.get('short_content_ru')
        instance.short_content_uz = self.context['request'].data.get('short_content_uz')
        instance.image = self.context['request'].FILES.get('image')

        instance.save()
        return instance
