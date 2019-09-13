from rest_framework.serializers import ModelSerializer

from app.model import Forms, Type_form


class ReformSerializer(ModelSerializer):
    class Meta:
        model = Forms
        fields = ('title_name_uz',
                  'title_name_ru',
                  'full_content_uz',
                  'full_content_ru',
                  'short_content_ru',
                  'short_content_uz',
                  'image',)

    def create(self, validated_data):
        news = Forms(**validated_data)
        request = self.context['request']
        type_id = request.data.get('type')
        type = Type_form.objects.get(id=type_id)
        news.type = type
        news.save()
        return news

    def update(self, instance, validated_data):

        instance.title_name_uz = self.context['request'].data.get('title_name_uz')
        instance.title_name_ru = self.context['request'].data.get('title_name_ru')
        instance.short_content_ru = self.context['request'].data.get('short_content_ru')
        instance.short_content_uz = self.context['request'].data.get('short_content_uz')
        instance.full_content_uz = self.context['request'].data.get('full_content_uz')
        instance.full_content_ru = self.context['request'].data.get('full_content_ru')
        instance.image = self.context['request'].FILES.get('image')
        request = self.context['request']
        type_id = request.data.get('type')
        type = Type_form.objects.get(id=int(type_id))
        instance.type = type
        instance.save()
        return instance


class Type_formSerialzier(ModelSerializer):
    class Meta:
        model = Type_form
        fields = ('name_ru',
                  'name_uz')