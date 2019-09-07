from rest_framework.serializers import ModelSerializer

from app.model import Menu
from app.model.menu import Submenu, Type_news, Type_form, News, Forms, Criminal, Type


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ('name_ru',)


class SubmenuSerializer(ModelSerializer):
    class Meta:
        model = Submenu
        fields = ('menu', 'name_ru',)

    def create(self, validated_data):
        request = self.context['request']
        s = Submenu(**validated_data)
        type_sub = request.data.get('type')
        t = Type.objects.get(id=type_sub)
        s.type = t
        s.save()
        return s




# class ContentSerializer(ModelSerializer):
#     class Meta:
#         model = None
#         fields = ()
#
#     def create(self, validated_data):
#         request = self.context['request']
#         submenu_id = request.data.get('sub_id')
#         detail_num = request.data.get('detail_num')
#         t = Submenu.objects.get(id=submenu_id)
#         if t.type == 1:
#             type_s = Type_detail.objects.get(id=detail_num)
#             if type_s ==1:
#                 type_submenu = Detail_1_Content.objects.create(submenu=t)
#                 fields = ('name_ru_title', 'name_ru_description')
#             elif type_s == 2:
#                 type_submenu = Detail_2_Content.objects.create(submenu=t)
#                 fields = ('full_name','name_ru_position', 'name_ru_phone', 'name_ru_admition_days')
#             elif type_s == 3:
#                 type_submenu = Detail_3_Content.objects.create(submenu=t)
#

            # list = {'1':Detail_1_Content,'2':Detail_2_Content, '3':Detail_3_Content}
            # list(t.type_s)
