from django.core.management.base import BaseCommand

from ...models import Player


class Command(BaseCommand):
    """Command update faceit stats"""

    help = "Update faceit stats"

    def handle(self, *args, **options):
        for player in Player.objects.all():
            player.save()
