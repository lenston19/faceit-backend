from rest_framework import serializers

from ..models import CSGOStats, DOTA2Stats, Faculty, Group, Player


class DOTA2StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DOTA2Stats
        fields = "__all__"


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
    dota2_stats = DOTA2StatsSerializer()
    group = GroupSerializer()

    class Meta:
        model = Player
        fields = "__all__"
