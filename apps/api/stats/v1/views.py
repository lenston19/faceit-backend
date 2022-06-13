from rest_framework.generics import ListAPIView, RetrieveAPIView

from ..models import Player, Group, Faculty
from .serializers import PlayerSerializer,GroupSerializer, FacultySerializer


class PlayerListApiView(ListAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


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
