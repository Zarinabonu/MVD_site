from django.db import models
from .criminal_static import Criminal_type


class Menu(models.Model):
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_uz = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('-id',)
        db_table = 'menu'

    def __str__(self):
        return self.name_ru



class   Submenu(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey('Type',on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
        db_table = 'submenu'

    def __str__(self):
        return self.name_ru


class Type(models.Model):
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_uz = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        ordering = ('-id',)
        db_table = 'type'

    def __str__(self):
        return self.name_ru


class Type_news(models.Model):
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_uz = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        ordering = ('-id',)
        db_table = 'type_news'

    def __str__(self):
        return self.name_ru


class Type_form(models.Model):
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_uz = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        ordering = ('-id',)
        db_table = 'type_form'

    def __str__(self):
        return self.name_ru


class News(models.Model):
    title_name_uz = models.CharField(max_length=255, null=True, blank=True)
    title_name_ru = models.CharField(max_length=255, null=True, blank=True)
    full_content_uz = models.TextField(null=True, blank=True)
    full_content_ru = models.TextField(null=True, blank=True)
    short_content_ru = models.TextField(null=True, blank=True)
    short_content_uz = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    type = models.ForeignKey('Type_news', on_delete=models.CASCADE, null=True, blank=True)


class Forms(models.Model):
    title_name_uz = models.CharField(max_length=255, null=True, blank=True)
    title_name_ru = models.CharField(max_length=255, null=True, blank=True)
    full_content_uz = models.TextField(null=True, blank=True)
    full_content_ru = models.TextField(null=True, blank=True)
    short_content_ru = models.TextField(null=True, blank=True)
    short_content_uz = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    type = models.ForeignKey('Type_form', on_delete=models.CASCADE)


class Criminal(models.Model):
    full_content_uz = models.TextField(null=True, blank=True)
    full_content_ru = models.TextField(null=True, blank=True)
    short_content_ru = models.TextField(null=True, blank=True)
    short_content_uz = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)



