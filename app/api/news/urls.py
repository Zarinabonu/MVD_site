from django.urls import path, include

from app.api.news import views

urlpatterns = [
    path('create/', views.NewsCreateAPIView.as_view(), name='api-news-create'),
    path('update/<int:id>', views.NewsUpdateAPIView.as_view(), name='api-news-update'),
    path('delete/<int:id>', views.NewsDeleteAPIView.as_view(), name='api-news-delete'),
    path('list/', views.NewsListAPIView.as_view(), name='api-news-list'),
    path('type/create/', views.News_typeCreateAPIView.as_view(), name='api-news-type-create'),
    path('type/update/<int:id>', views.News_typeUpdateAPIView.as_view(), name='api-news-type-update'),
    path('type/delete/<int:id>', views.News_typeDeleteAPIView.as_view(), name='api-news-type-delete'),

]