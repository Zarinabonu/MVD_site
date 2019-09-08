from rest_framework.serializers import ModelSerializer

from app.model import News


class NewsSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_ru', 'description_name_ru')

    def update(self, instance, validated_data):

        print('AAAAA',validated_data.get('description_name_ru'))
        print('1111',self.context['request'].data.get('description_name_ru'))
        instance.title_name_ru = self.context['request'].data.get('title_name_ru')
        instance.description_name_ru = self.context['request'].data.get('description_name_ru')
        print(' DDDD',instance.description_name_ru)

        instance.save()
        print('     BBBB',instance.description_name_ru)
        print('22222',self.context['request'].data.get('description_name_ru'))

        return instance

class NewsCreateSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_ru', 'description_name_ru', 'type')

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


class NewsListSerialzier(ModelSerializer):
    class Meta:
        model = News
        fields = ('title_name_ru', 'description_name_ru', 'type')
