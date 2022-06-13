from django.urls import path

from .views import (
    FacultyListApiView,
    GroupListApiView,
    PlayerListApiView,
    PlayerRetrieveAPIView,
)

app_name = "stats"

urlpatterns = [
    path("player/", PlayerListApiView.as_view(), name="player-list"),
    path(
        "player/<int:id>",
        PlayerRetrieveAPIView.as_view(),
        name="player-detail",
    ),
    path("group/", GroupListApiView.as_view(), name="group-list"),
    path("faculty/", FacultyListApiView.as_view(), name="faculty-list"),
]
