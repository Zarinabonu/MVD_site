from django.contrib import admin

from app.model.menu import Submenu
from .model import News, Type_news, Type_form, Menu, News, Menu,Forms, Criminal, Type, Region, Criminal_type, Static_criminal, International_busines


admin.site.register(Menu)
admin.site.register(Submenu)
admin.site.register(Type_form)
admin.site.register(News)
admin.site.register(Forms)
admin.site.register(Criminal)
admin.site.register(Type_news)
admin.site.register(Type)
admin.site.register(Region)
admin.site.register(Criminal_type)
admin.site.register(Static_criminal)
admin.site.register(International_busines)

# admin.site.registadmin.site.register(Type_news)er(Submenu)
# Register your models here.
