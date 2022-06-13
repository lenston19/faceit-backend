from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CSGOStats, Player
from .utils import FaceitAPI


@receiver(post_save, sender=Player)
def fetch_player_stats(sender, instance: Player, **kwargs):
    faceit_instance = FaceitAPI(instance.nickname)
    faceit_stats = faceit_instance.player_stats()
    faceit_info = faceit_instance.player_information()
    CSGOStats.objects.update_or_create(
        player_id=instance.pk,
        kd_ratio=faceit_stats["lifetime"]["K/D Ratio"],
        average_kd_ratio=faceit_stats["lifetime"]["Average K/D Ratio"],
        elo=faceit_info["games"]["csgo"]["faceit_elo"],
        average_hs=faceit_stats["lifetime"]["Average Headshots %"],
        win_rate=faceit_stats["lifetime"]["Win Rate %"],
    )
