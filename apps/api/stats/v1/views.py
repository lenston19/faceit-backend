from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import Faculty, Group, Player
from .serializers import FacultySerializer, GroupSerializer, PlayerSerializer


class PlayerListApiView(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("group", "group__faculty")


class PlayerRetrieveAPIView(RetrieveAPIView):
    serializer_class = PlayerSerializer
    queryset = Player
    lookup_url_kwarg = "id"


class FacultyListApiView(ListAPIView):
    serializer_class = FacultySerializer
    queryset = Faculty.objects.all()


class GroupListApiView(ListAPIView):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
