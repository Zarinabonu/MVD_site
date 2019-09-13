from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from app.model import Forms, Type_form

from app.api.reforms.serializers import ReformSerializer, Type_formSerialzier
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


class Form_typeCreateAPIView(CreateAPIView):
    queryset = Type_form. objects.all()
    serializer_class = Type_formSerialzier


class Form_typeUpdateAPIView(UpdateAPIView):
    queryset = Type_form. objects.all()
    serializer_class = Type_formSerialzier
    lookup_url_kwarg = 'id'


class Form_typeDeleteAPIView(DestroyAPIView):
    queryset = Type_form. objects.all()
    serializer_class = Type_formSerialzier
    lookup_url_kwarg = 'id'

