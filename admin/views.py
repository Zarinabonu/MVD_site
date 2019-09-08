from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from app.model import News, Type_news, Forms, Type_form

class Admin(View):
	def get(self, request):
		return render(request, 'admin/index.html')

class News_ListView(ListView):
    # template_name = 'home.html'
    # model = News
    # context_object_name = 'news'
    def get(self, request, *args, **kwargs):
        news = News.objects.all()[:4]
        return render(request, 'admin/news/list.html', {'news': news})


class News_CreateView(View):

    def get(self, request, *args, **kwargs):
        news = News.objects.all()[:4]
        types = Type_news.objects.all()
        return render(request, 'admin/news/create.html', {'news': news,
        	'type':types})


class News_UpdateView(DetailView):
	template_name = 'admin/news/update.html'
	model = News
	context_object_name = 'update_news'
	pk_url_kwarg = 'id'


class Reform_ListView(ListView):

    def get(self, request, *args, **kwargs):
        reform = Forms.objects.all()[:4]
        type = Type_form.objects.all()
        return render(request, 'admin/reform/list.html', {'reforms': reform,
        	'types':types})

class Reform_UpdateView(DetailView):
	form = Forms.objects.all()
	pk_url_kwarg = 'id'

	def get(self, request, *args, **kwargs):
		type = Type_form.objects.all()
		return render(request, 'admin/reform/update.html', {'types':type,
			'forms': form})



# Create your views here.
