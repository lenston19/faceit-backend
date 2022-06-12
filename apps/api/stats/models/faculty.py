from django.db import models
from django.utils.translation import ugettext_lazy as _


class Faculty(models.Model):
    """
    Факультет
    """

    name = models.CharField(_("Наименование факультета"), max_length=250)

    class Meta:
        verbose_name = _("Факультет")
        verbose_name_plural = _("Факультеты")

    def __str__(self):
        return self.name
