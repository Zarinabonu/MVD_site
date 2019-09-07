from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from app.model import News, Forms, Criminal


class News_ListView(ListView):
    # template_name = 'home.html'
    # model = News
    # context_object_name = 'news'
    def get(self, request, *args, **kwargs):
        news = News.objects.all()[:4]
        reform = Forms.objects.all()[:4]
        criminal = Criminal.objects.all()[:5]
        return render(request, 'home.html', {'news': news,
                                             'reforms': reform,
                                             'criminals': criminal})

# Create your views here.
