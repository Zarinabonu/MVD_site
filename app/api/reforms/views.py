from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from app.model import Forms

from app.api.reforms.serializers import ReformSerializer, ReformListSerializer
from app.model import News


class ReformNewsCreateAPIView(CreateAPIView):
    queryset = Forms. objects.all()
    serializer_class = ReformSerializer


class ReformUpdateAPIView(UpdateAPIView):
    queryset = Forms. objects.all()
    serializer_class = ReformSerializer
    lookup_url_kwarg = 'id'


class ReformDeleteAPIView(DestroyAPIView):
    queryset = Forms. objects.all()
    serializer_class = ReformSerializer
    lookup_url_kwarg = 'id'


class ReformListAPIView(ListAPIView):
    queryset = Forms. objects.all()
    serializer_class = ReformListSerializer
