from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Sum
from app.model import News, Forms, Criminal, Static_criminal, Region, Criminal_type, International_busines, Type_news, \
    Type_form


class News_ListView(ListView):

    def get(self, request, *args, **kwargs):
        list = []
        list2 = []
        list3 = []
        list4 = []
        list_news_type =[]
        list_news = []


        news = News.objects.all()
        news_type = Type_news.objects.all()
        for t_news in news_type:
            new_type = news.filter(type=t_news)
            list_news_type.append(t_news)
            list_news.append(new_type)
        # response_news = [{'news_type': n_type, 'news': new} for n_type, new in zip(list7, list8)]

        reform = Type_form.objects.all()[:4]
        criminal = Criminal.objects.all()[:5]

        static = Static_criminal.objects.all()
        region = Region.objects.all()
        criminal_type = Criminal_type.objects.all()
        for city in region:
            s = Static_criminal.objects.filter(region=city)
            c = s.aggregate(Sum('counter'))
            list.append(c)
            list2.append(city)
        response = [{'City': c, 'count': counts} for c, counts in zip(list2, list)]

        for criminals in criminal_type:
            criminal_static = Static_criminal.objects.filter(criminal_type=criminals)
            list3.append(criminals)
            list4.append(criminal_static.count())
        response2 = [{'criminal_type': cri, 'criminal_count': criminal_counts} for cri, criminal_counts in zip(list3, list4)]

        return render(request, 'home.html', {'news_type': news_type,
                                             'subnew':list_news,
                                             'reforms': reform,
                                             'criminals': criminal,
                                             'cities': response,
                                             'criminal_count':response2})


class News_Detail_ListView(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super(News_Detail_ListView, self).get_context_data(**kwargs)
        context['internationals'] = International_busines.objects.all()


        return context


class International_detailView(DetailView):
    template_name = 'newspodrobni.html'
    pk_url_kwarg = 'id'
    model = International_busines







# Create your views here.
