from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from app.model import Forms

from app.api.criminal.serializers import CriminalSerializer, CriminalListSerializer
from app.model import Criminal


class CriminalNewsCreateAPIView(CreateAPIView):
    queryset = Criminal. objects.all()
    serializer_class = CriminalSerializer


class CriminalUpdateAPIView(UpdateAPIView):
    queryset = Criminal. objects.all()
    serializer_class = CriminalSerializer
    lookup_url_kwarg = 'id'


class CriminalDeleteAPIView(DestroyAPIView):
    queryset = Criminal. objects.all()
    serializer_class = CriminalSerializer
    lookup_url_kwarg = 'id'


class CriminalListAPIView(ListAPIView):
    queryset = Criminal. objects.all()
    serializer_class = CriminalListSerializer
