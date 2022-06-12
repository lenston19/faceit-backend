from django.db import models
from django.utils.translation import ugettext_lazy as _

from .csgo_stats import CSGOStats
from .group import Group


class Player(models.Model):
    """
    Игрок
    """

    first_name = models.CharField(_("Имя"), max_length=30, blank=True)

    last_name = models.CharField(_("Фамилия"), max_length=150, blank=True)

    patronymic = models.CharField(_("Отчество"), max_length=150, blank=True)

    nickname = models.CharField(_("Никнейм"), max_length=150)

    stats = models.ForeignKey(CSGOStats, verbose_name=_("Статистика игрока"), on_delete=models.CASCADE)

    group = models.ForeignKey(Group, verbose_name=_("Учебная группа"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Игрок")
        verbose_name_plural = _("Игроки")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
