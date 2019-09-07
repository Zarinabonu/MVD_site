from django.urls import path, include

from app.api.news import views

urlpatterns = [
    path('create/', views.NewsCreateAPIView.as_view(), name='api-news-create'),
    path('update/<int:id>', views.NewsUpdateAPIView.as_view(), name='api-news-update'),
    path('delete/<int:id>', views.NewsDeleteAPIView.as_view(), name='api-news-delete'),
    path('list/', views.NewsListAPIView.as_view(), name='api-news-list'),

]