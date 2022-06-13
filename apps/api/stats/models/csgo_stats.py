from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .player import Player


class CSGOStats(models.Model):
    """
    Статистика CS:GO
    """

    player = models.OneToOneField(
        Player,
        verbose_name=_("Игрок"),
        on_delete=models.CASCADE,
        related_name="csgo_stats",
        null=True,
    )

    elo = models.PositiveSmallIntegerField(_("ELO"), blank=True)

    kd_ratio = models.FloatField(_("K/D Ratio"), blank=True)

    average_kd_ratio = models.FloatField(_("Average K/D Ratio"), blank=True)

    average_hs = models.PositiveSmallIntegerField(
        _("Average Headshots %"),
        validators=[MaxValueValidator(100)],
        blank=True,
    )

    win_rate = models.PositiveSmallIntegerField(
        _("Win Rate %"), validators=[MaxValueValidator(100)], blank=True
    )

    class Meta:
        verbose_name = _("Статистика CS:GO")
        verbose_name_plural = _("Статистика CS:GO")

    def __str__(self):
        return f"{self.player_id} {self.elo}"
