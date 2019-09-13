from rest_framework.serializers import ModelSerializer

from app.model import News, Type_news


class NewsSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_uz',
                  'title_name_ru',
                  'full_content_uz',
                  'full_content_ru',
                  'short_content_ru',
                  'short_content_uz',
                  )

    def create(self, validated_data):
        news = News(**validated_data)
        request = self.context['request']
        type_id = request.data.get('type')
        type = Type_news.objects.get(id=type_id)
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
        request = self.context['request']
        type_id = request.data.get('type')
        type = Type_news.objects.get(id=type_id)
        instance.type = type
        instance.save()
        return instance


class NewsCreateSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_uz',
                  'title_name_ru',
                  'full_content_uz',
                  'full_content_ru',
                  'short_content_ru',
                  'short_content_uz',
                  'type')


class Type_newsSerialzier(ModelSerializer):
    class Meta:
        model = Type_news
        fields = ('name_ru',
                  'name_uz')
    # def create(self,validated_data):
    #     news = News(validated_data)
    #     print('AAAAA',validated_data.get('title_name_ru'))

    #     t = self.context['request'].data.get('title_name_ru')
    #     d = self.context['request'].data.get('description_name_ru')
    #     ty = self.context['request'].data.get('type')
    #     news.title_name_ru = t
    #     news.description_name_ru = d
    #     news.type = ty
    #     news.save()
    #     print('1111', t,d,ty)
    #     return news


# class NewsListSerialzier(ModelSerializer):
#     class Meta:
#         model = News
#         fields = ('title_name_ru', 'description_name_ru', 'type')
