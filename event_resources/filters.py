import re

from django import template

register = template.Library()

@register.filter
def youtube_id(value):
    match = re.search(r"[?&]v=([^&#]*)", value)
    return match.group(1) if match else None