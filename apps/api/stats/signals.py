from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import CSGOStats, DOTA2Stats, Player
from .utils import FaceitAPI


@receiver(pre_save, sender=Player)
def fetch_faceit_id(sender, instance: Player, **kwargs):
    try:
        faceit_instance = FaceitAPI(instance.nickname, "csgo")
        instance.faceit_id = faceit_instance.player_id
        faceit_instance = FaceitAPI(instance.nickname, "dota2")
        instance.faceit_id = faceit_instance.player_id
    except:
        pass


@receiver(post_save, sender=Player)
def fetch_player_stats(sender, instance: Player, **kwargs):
    try:
        faceit_instance = FaceitAPI(instance.nickname, "csgo")
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
    except:
        pass
    try:
        faceit_instance = FaceitAPI(instance.nickname, "dota2")
        faceit_stats = faceit_instance.player_stats()
        faceit_info = faceit_instance.player_information()
        DOTA2Stats.objects.update_or_create(
            player_id=instance.pk,
            kd_ratio=faceit_stats["lifetime"]["K/D Ratio"],
            average_kd_ratio=faceit_stats["lifetime"]["Average K/D Ratio"],
            elo=faceit_info["games"]["dota2"]["faceit_elo"],
            average_gm=faceit_stats["lifetime"]["Average Gold/minute"],
            win_rate=faceit_stats["lifetime"]["Win Rate %"],
        )
    except:
        pass
