from django.contrib.admin import ModelAdmin, register

from apps.core.utils.admin import BaseAdminMixin

from .models import CSGOStats, Faculty, Group, Player


@register(Player)
class PlayerAdmin(ModelAdmin, BaseAdminMixin):
    list_display = ("first_name", "last_name", "patronymic")


@register(Faculty)
class FacultyAdmin(ModelAdmin, BaseAdminMixin):
    list_display = ("name",)


@register(Group)
class GroupAdmin(ModelAdmin, BaseAdminMixin):
    list_display = ("name",)


@register(CSGOStats)
class CSGOStatsAdmin(ModelAdmin, BaseAdminMixin):
    list_display = (
        "name",
        "player_id",
        "elo",
        "kd_ratio",
        "average_kd_ratio",
        "average_hs",
        "win_rate",
    )

    list_filter = (
        "elo",
        "kd_ratio",
        "average_kd_ratio",
        "average_hs",
        "win_rate",
    )
