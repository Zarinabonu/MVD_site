from django.db import models


class Region(models.Model):
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        db_table = 'region'

    def __str__(self):
        return self.name_ru


class Criminal_type(models.Model):
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        db_table = 'criminal_type'

    def __str__(self):
        return self.name_ru


class Static_criminal(models.Model):
    region = models.ManyToManyField('Region')
    criminal_type = models.ForeignKey('Criminal_type', null=True, blank=True, on_delete=models.DO_NOTHING)
    counter = models.IntegerField(null=True, blank=True)