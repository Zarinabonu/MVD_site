from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.model import Menu
from .serializers import MenuSerializer


class MenuCreateAPIView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer