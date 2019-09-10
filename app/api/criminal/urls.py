from django.urls import path, include

from app.api.criminal import views

urlpatterns = [
    path('create/', views.CriminalNewsCreateAPIView.as_view(), name='api-criminal-create'),
    path('update/<int:id>', views.CriminalUpdateAPIView.as_view(), name='api-criminal-update'),
    path('delete/<int:id>', views.CriminalDeleteAPIView.as_view(), name='api-criminal-delete'),
    path('list/', views.CriminalListAPIView.as_view(), name='api-criminal-list'),
    path('static/', views.Criminal_staticCreateAPIView.as_view(), name='api-criminal-static'),

]
