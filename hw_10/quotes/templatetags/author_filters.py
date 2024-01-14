# templatetags/author_filters.py
from django import template
from ..utils import get_author

register = template.Library()

@register.filter(name='author')
def author_filter(author_id):
    return get_author(author_id)