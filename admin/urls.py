from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from admin import views

urlpatterns = [
    path('', views.Admin.as_view(), name='admin'),
    path('news/list', views.News_ListView.as_view(), name='news-list'),
    path('news/create', views.News_CreateView.as_view(), name='news-create'),
    path('news/update/<int:id>', views.News_UpdateView.as_view(), name='news-update'),
    path('reform', views.Reform_ListView.as_view(), name='reform'),
    path('reform/update/<int:id>', views.Reform_UpdateView.as_view(), name='reform-update'),
    path('reform/create', views.Reform_CreateView.as_view(), name='form-create'),
    path('criminal/list', views.Criminal_ListView.as_view(), name='criminal-list'),
    path('criminal/update/<int:id>', views.Criminal_UpdateView.as_view(), name='crimanl-update'),
    path('criminal/create', views.Criminal_CreateView.as_view(), name='criminal-create'),

]