from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StatsConfig(AppConfig):
    """Default app config"""

    name = "apps.api.stats"
    verbose_name = _("Статистика")
