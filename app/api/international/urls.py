from django.urls import path, include

from app.api.international import views

urlpatterns = [
    path('create/', views.InternationalCreateAPIView.as_view(), name='api-international-create'),
    path('update/<int:id>', views.InternationalUpdateAPIView.as_view(), name='api-international-update'),
    path('delete/<int:id>', views.InternationalDeleteAPIView.as_view(), name='api-international-delete'),
    path('list/', views.InternationalListAPIView.as_view(), name='api-international-list'),

]