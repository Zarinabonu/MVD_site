from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from app.model import Menu
from app.model.menu import Submenu, News
from .serializers import MenuSerializer, SubmenuSerializer


class MenuCreateAPIView(CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SubmenuCreateAPIView(CreateAPIView):
    queryset = Submenu.objects.all()
    serializer_class = SubmenuSerializer


