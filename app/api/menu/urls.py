from django.urls import path, include

from app.api.menu import views

urlpatterns = [
    path('menu/', views.MenuCreateAPIView.as_view(), name='api-menu-create'),
    path('submenu/', views.SubmenuCreateAPIView.as_view(), name='api-submenu-create'),

]