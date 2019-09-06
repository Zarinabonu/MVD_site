from django.db import models


class Menu(models.Model):
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_uz = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        ordering = ('-id',)
        db_table = 'menu'

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


class Submenu(models.Model):
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)
    name_uz = models.CharField(max_length=100, null=True, blank=True)
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey('Type',on_delete=models.CASCADE)

    class Meta:
        ordering = ('-id',)
        db_table = 'submenu'

    def __str__(self):
        return self.name_ru


class ListContent(models.Model):
    submenu = models.ForeignKey('Submenu', on_delete=models.CASCADE)
    name_uz_title = models.CharField(max_length=100, null=True, blank=True)
    name_ru_title = models.CharField(max_length=100, null=True, blank=True)
    name_uz_description = models.CharField(max_length=100, null=True, blank=True)
    name_ru_description = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    view = models.IntegerField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    file = models.FileField(null=True, blank=True)


class DetailContent(models.Model):
    submenu = models.OneToOneField('Submenu', on_delete=models.CASCADE)
    name_uz_title = models.CharField(max_length=100, null=True, blank=True)
    name_ru_title = models.CharField(max_length=100, null=True, blank=True)
    name_uz_description = models.CharField(max_length=100, null=True, blank=True)
    name_ru_description = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    view = models.IntegerField()
    image = models.ImageField()
    date = models.DateField(auto_now_add=True)
    file = models.FileField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)



