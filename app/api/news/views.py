from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.news.serializers import NewsSerialzier, NewsCreateSerialzier, Type_newsSerialzier
from app.model import News, Type_news


class NewsCreateAPIView(CreateAPIView):
    queryset = News. objects.all()
    serializer_class = NewsCreateSerialzier


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
    serializer_class = NewsSerialzier


class News_typeCreateAPIView(CreateAPIView):
    queryset = Type_news. objects.all()
    serializer_class = Type_newsSerialzier


class News_typeUpdateAPIView(UpdateAPIView):
    queryset = Type_news. objects.all()
    serializer_class = Type_newsSerialzier
    lookup_url_kwarg = 'id'


class News_typeDeleteAPIView(DestroyAPIView):
    queryset = Type_news. objects.all()
    serializer_class = Type_newsSerialzier
    lookup_url_kwarg = 'id'
