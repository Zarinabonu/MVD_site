from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from app.model import News, Type_news, Forms, Type_form, Criminal


class Admin(View):
	def get(self, request):
		return render(request, 'cms/index.html')

class News_ListView(ListView):
    # template_name = 'home.html'
    # model = News
    # context_object_name = 'news'
    def get(self, request, *args, **kwargs):
        news = News.objects.all()[:4]
        return render(request, 'cms/news/list.html', {'news': news})


class News_CreateView(View):

    def get(self, request, *args, **kwargs):
        news = News.objects.all()[:4]
        types = Type_news.objects.all()
        return render(request, 'cms/news/create.html', {'news': news,
        	'type':types})


class News_UpdateView(DetailView):
	template_name = 'cms/news/update.html'
	model = News
	context_object_name = 'update_news'
	pk_url_kwarg = 'id'


class Reform_ListView(ListView):
    def get(self, request, *args, **kwargs):
        reform = Forms.objects.all()[:4]
        type = Type_form.objects.all()
        return render(request, 'cms/reform/list.html', {'reforms': reform,
        	'types':type})


class Reform_UpdateView(DetailView):

	model = Forms
	context_object_name = 'reform'
	template_name = 'cms/reform/update.html'
	pk_url_kwarg = 'id'

	def get_context_data(self, **kwargs):
		context = super(Reform_UpdateView, self).get_context_data(**kwargs)
		context['type'] = Type_form.objects.all()
		return context


class Reform_CreateView(TemplateView):
	template_name = 'cms/reform/create.html'

	def get_context_data(self, **kwargs):
		context = super(Reform_CreateView, self).get_context_data(**kwargs)
		context['type'] = Type_form.objects.all()
		return context


class Criminal_ListView(ListView):
	model = Criminal
	context_object_name = 'criminal'
	template_name = 'cms/criminal/list.html'
	queryset = Criminal.objects.all()


class Criminal_UpdateView(DetailView):
	model = Criminal
	context_object_name = 'criminal'
	template_name = 'cms/criminal/update.html'
	pk_url_kwarg = 'id'


class Criminal_CreateView(TemplateView):
	template_name = 'cms/criminal/create.html'








# Create your views here.
