from django.urls import path, include

from app.api.menu import views

urlpatterns = [
    path('create/', views.MenuCreateAPIView.as_view(), name='api-menu-create')
]