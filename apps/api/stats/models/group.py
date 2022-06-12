from django.db import models
from django.utils.translation import ugettext_lazy as _

from .faculty import Faculty


class Group(models.Model):
    """
    Группа
    """

    name = models.CharField(_("Наименование группы"), max_length=250)

    faculty = models.ForeignKey(
        Faculty, verbose_name=_("Факультет"), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")

    def __str__(self):
        return self.name
