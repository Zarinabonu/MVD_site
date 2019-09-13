from django.db import models


class Region(models.Model):
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-id',)
        db_table = 'region'

    def __str__(self):
        return self.name_ru


class Criminal_type(models.Model):
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(upload_to='media', null=True, blank=True)
    count = models.IntegerField(default=0)

    class Meta:
        ordering = ('-id',)
        db_table = 'criminal_type'

    def __str__(self):
        return self.name_ru


#class Static_criminal(models.Model):
#    region = models.ManyToManyField('Region')
#    counter = models.IntegerField(default=0)
