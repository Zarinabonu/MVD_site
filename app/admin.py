from django.contrib import admin

from app.model.menu import Submenu
from .model import News, Type_news, Type_form, Menu, News, Menu,Forms, Criminal, Type

admin.site.register(Menu)
admin.site.register(Submenu)
admin.site.register(Type_form)
admin.site.register(News)
admin.site.register(Forms)
admin.site.register(Criminal)
admin.site.register(Type_news)
admin.site.register(Type)

# admin.site.registadmin.site.register(Type_news)er(Submenu)
# Register your models here.