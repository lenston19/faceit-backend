from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .player import Player


class DOTA2Stats(models.Model):
    """
    Статистика DOTA 2
    """

    player = models.OneToOneField(
        Player,
        verbose_name=_("Игрок"),
        on_delete=models.CASCADE,
        related_name="dota2_stats",
        null=True,
    )

    elo = models.PositiveSmallIntegerField(_("ELO"), blank=True)

    kd_ratio = models.FloatField(_("K/D Ratio"), blank=True)

    average_kd_ratio = models.FloatField(_("Average K/D Ratio"), blank=True)

    average_gm = models.FloatField(
        _("Average Gold/minute"),
        blank=True,
    )

    win_rate = models.PositiveSmallIntegerField(
        _("Win Rate %"), validators=[MaxValueValidator(100)], blank=True
    )

    class Meta:
        verbose_name = _("Статистика DOTA 2")
        verbose_name_plural = _("Статистика DOTA 2")

    def __str__(self):
        return f"{self.player_id} {self.elo}"
