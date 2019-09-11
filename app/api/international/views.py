from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from app.model import Forms

from app.api.international.serializers import InternationalSerializer
from app.model import International_busines


class InternationalCreateAPIView(CreateAPIView):
    queryset = International_busines. objects.all()
    serializer_class = InternationalSerializer


class InternationalUpdateAPIView(UpdateAPIView):
    queryset = International_busines. objects.all()
    serializer_class = InternationalSerializer
    lookup_url_kwarg = 'id'


class InternationalDeleteAPIView(DestroyAPIView):
    queryset = International_busines. objects.all()
    serializer_class = InternationalSerializer
    lookup_url_kwarg = 'id'


class InternationalListAPIView(ListAPIView):
    queryset = International_busines. objects.all()
    serializer_class = InternationalSerializer
