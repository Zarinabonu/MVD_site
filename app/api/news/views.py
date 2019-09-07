from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.news.serializers import NewsSerialzier, NewsListSerialzier
from app.model import News


class NewsCreateAPIView(CreateAPIView):
    queryset = News. objects.all()
    serializer_class = NewsSerialzier


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News. objects.all()
    serializer_class = NewsSerialzier
    lookup_url_kwarg = 'id'


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News. objects.all()
    serializer_class = NewsSerialzier
    lookup_url_kwarg = 'id'


class NewsListAPIView(ListAPIView):
    queryset = News. objects.all()
    serializer_class = NewsListSerialzier
