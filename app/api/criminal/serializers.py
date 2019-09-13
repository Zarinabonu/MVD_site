from rest_framework.serializers import ModelSerializer

from app.model import Criminal

from app.model import  Criminal_type, Region



class CriminalSerializer(ModelSerializer):
    class Meta:
        model = Criminal
        fields = ('full_content_uz',
                  'full_content_ru',
                  'short_content_ru',
                  'short_content_uz',
                  'image')

    def update(self, instance, validated_data):

        instance.short_content_ru = self.context['request'].data.get('short_content_ru')
        instance.short_content_uz = self.context['request'].data.get('short_content_uz')
        instance.full_content_uz = self.context['request'].data.get('full_content_uz')
        instance.full_content_ru = self.context['request'].data.get('full_content_ru')
        instance.image = self.context['request'].FILES.get('image')

        instance.save()
        return instance


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ()

    def update(self, instance, validated_data):
        instance.count = self.context['request'].data.get('count')

        instance.save()
        return instance


class Criminal_typeSerializer(ModelSerializer):
    class Meta:
        model = Criminal_type
        fields = ('name_uz',
                  'name_ru',
                  'icon',
                  'count')

    def update(self, instance, validated_data):

        instance.name_uz = self.context['request'].data.get('name_uz')
        instance.name_ru = self.context['request'].data.get('name_ru')
        instance.icon = self.context['request'].FILES.get('icon')
        instance.count = self.context['request'].data.get('count')

        instance.save()
        return instance

