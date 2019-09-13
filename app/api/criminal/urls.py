from django.urls import path, include

from app.api.criminal import views

urlpatterns = [
    path('create/', views.CriminalNewsCreateAPIView.as_view(), name='api-criminal-create'),
    path('update/<int:id>', views.CriminalUpdateAPIView.as_view(), name='api-criminal-update'),
    path('delete/<int:id>', views.CriminalDeleteAPIView.as_view(), name='api-criminal-delete'),
    path('type/create', views.Criminal_typeCreateAPIView.as_view(), name='api-criminal-type-create'),
    path('type/update/<int:id>', views.Criminal_typeUpdateAPIView.as_view(), name='api-criminal-type-update'),
    path('type/delete/<int:id>', views.Criminal_typeDeleteAPIView.as_view(), name='api-criminal-type-delete'),
    path('region/update/<int:id>', views.RegionUpdateAPIView.as_view(), name='api-criminal-region-update'),

]
