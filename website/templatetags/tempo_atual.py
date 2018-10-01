import datetime
from django import template

register = template.Library()


@register.simple_tag
def tempo_atual():
    return datetime.datetime.now().strftime('%H:%M:%S')
#    return datetime.timezone.now(datetime.timedelta(hours=-6))
