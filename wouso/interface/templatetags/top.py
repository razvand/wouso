from django import template
from wouso.core.user.models import Race, Player

register = template.Library()


@register.simple_tag()
def top_10_races():
    return Race.objects.exclude(can_play=False).order_by('-points')[:10]


@register.simple_tag()
def top_10_players():
    return Player.objects.order_by('-points')[:10]
