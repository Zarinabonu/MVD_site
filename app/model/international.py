from django.db import models
from  django.contrib.auth.models import User


class International_busines(models.Model):
    title_name_ru = models.CharField(max_length=100, null=True, blank=True)
    title_name_uz = models.CharField(max_length=100, null=True, blank=True)
    full_content_uz = models.TextField(null=True, blank=True)
    full_content_ru = models.TextField(null=True, blank=True)
    short_content_uz = models.TextField(null=True, blank=True)
    short_content_ru = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    views = models.ManyToManyField(User)