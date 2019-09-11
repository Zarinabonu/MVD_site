from django.urls import path, include

from app.api.menu import views

urlpatterns = [
    path('menu/', include('app.api.menu.urls')),
    path('news/', include('app.api.news.urls')),
    path('reform/', include('app.api.reforms.urls')),
    path('criminal/', include('app.api.criminal.urls')),
    path('international/', include('app.api.international.urls')),

]