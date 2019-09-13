from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.db.models import Sum
from pure_pagination import PaginationMixin
from app.model import News, Forms, Criminal, Region, Criminal_type, International_busines, Type_news, \
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

        reform = Type_form.objects.all()[:4]
        criminal = Criminal.objects.all()[:5]

        region = Region.objects.all()
        criminal_type = Criminal_type.objects.all()


        return render(request, 'home.html', {'news_type': news_type,
                                             'subnew':list_news,
                                             'reforms': reform,
                                             'criminals': criminal_type,
                                             'incidents': criminal,
                                             'cities': region,
                                             })


class News_Detail_ListView(PaginationMixin, ListView):
    template_name = 'news.html'
    queryset = International_busines.objects.all()
    context_object_name = 'internationals'
    paginate_by = 12


class International_detailView(DetailView):
    template_name = 'newspodrobni.html'
    pk_url_kwarg = 'id'
    model = International_busines
    context_object_name = 'news_detail'







# Create your views here.
