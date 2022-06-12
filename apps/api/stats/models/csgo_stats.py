from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class CSGOStats(models.Model):
    """
    Статистика CS:GO
    """

    name = models.CharField(_("Наименование игры"), max_length=50)

    player_id = models.CharField(
        _("Уникальное значение игрока"), max_length=255
    )

    elo = models.PositiveSmallIntegerField(_("ELO"), blank=True)

    kd_ratio = models.FloatField(_("K/D Ratio"), blank=True)

    average_kd_ratio = models.FloatField(_("Average K/D Ratio"), blank=True)

    average_hs = models.PositiveSmallIntegerField(
        _("Average Headshots %"), validators=[MaxValueValidator(100)]
    )

    win_rate = models.PositiveSmallIntegerField(
        _("Win Rate %"), validators=[MaxValueValidator(100)]
    )

    class Meta:
        verbose_name = _("Статистика CS:GO")
        verbose_name_plural = _("Статистика CS:GO")

    def __str__(self):
        return f"{self.player_id} {self.elo}"
