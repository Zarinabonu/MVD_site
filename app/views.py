from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Sum
from app.model import News, Forms, Criminal, Static_criminal, Region, Criminal_type


class News_ListView(ListView):

    def get(self, request, *args, **kwargs):
        news = News.objects.all()[:4]
        reform = Forms.objects.all()[:4]
        criminal = Criminal.objects.all()[:5]
        list = []
        list2 = []
        static = Static_criminal.objects.all()
        region = Region.objects.all()
        criminal_type = Criminal_type.objects.all()
        for city in region:
            s = Static_criminal.objects.filter(region=city)
            c = s.aggregate(Sum('counter'))
            list.append(c)
            list2.append(city)
        print('LIST', list)
        response = [{'City': c, 'count': counts} for c, counts in zip(list2, list)]

        return render(request, 'home.html', {'news': news,
                                             'reforms': reform,
                                             'criminals': criminal,
                                             'cities': response})


class News_Detail_ListView(TemplateView):
    template_name = 'news.html'


class Criminal_static_ListView(ListView):

    def get(self, request, *args, **kwargs):

        response = [{'City': c, 'count': counts} for c, counts in zip(list, list2)]

        print('LISTS :', response)

        return render(request, 'home.html', {'reforms': reform,
                                             'criminals': criminal})



# Create your views here.
