from rest_framework import serializers

from ..models import CSGOStats, Faculty, Group, Player


class CSGOStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CSGOStats
        fields = "__all__"


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()

    class Meta:
        model = Group
        fields = "__all__"


class PlayerSerializer(serializers.ModelSerializer):
    csgo_stats = CSGOStatsSerializer()
    group = GroupSerializer()

    class Meta:
        model = Player
        fields = "__all__"
