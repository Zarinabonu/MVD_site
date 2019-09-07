from django.urls import path, include

from app.api.reforms import views

urlpatterns = [
    path('create/', views.ReformNewsCreateAPIView.as_view(), name='api-reform-create'),
    path('update/<int:id>', views.ReformUpdateAPIView.as_view(), name='api-reform-update'),
    path('delete/<int:id>', views.ReformDeleteAPIView.as_view(), name='api-reform-delete'),
    path('list/', views.ReformListAPIView.as_view(), name='api-reform-list'),

]