from django.urls import path, include

from app.api.menu import views

urlpatterns = [
    path('menu/', include('app.api.menu.urls'))
]