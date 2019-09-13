from django.urls import path, include

from app.api.reforms import views

urlpatterns = [
    path('create/', views.ReformNewsCreateAPIView.as_view(), name='api-reform-create'),
    path('update/<int:id>', views.ReformUpdateAPIView.as_view(), name='api-reform-update'),
    path('delete/<int:id>', views.ReformDeleteAPIView.as_view(), name='api-reform-delete'),
    path('type/create/', views.Form_typeCreateAPIView.as_view(), name='api-news-type-create'),
    path('type/update/<int:id>', views.Form_typeUpdateAPIView.as_view(), name='api-news-type-update'),
    path('type/delete/<int:id>', views.Form_typeDeleteAPIView.as_view(), name='api-news-type-delete'),

]