from django.db import models
from  django.contrib.auth.models import User


class International_busines(models.Model):
    title_ru = models.CharField(max_length=100, null=True, blank=True)
    title_uz = models.CharField(max_length=100, null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    description_uz = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    views = models.ManyToManyField(User)