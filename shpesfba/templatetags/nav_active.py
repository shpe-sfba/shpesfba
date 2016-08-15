import re

from django import template
from django.core.urlresolvers import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(name='nav_active', takes_context=True)
def nav_active(context, pattern_or_urlname, css_class):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname

    if 'request' not in context:
        return ''

    path = context['request'].path

    if path in ('', '/') and pattern_or_urlname == 'index':
        return css_class
    elif path not in ('', '/') and pattern_or_urlname == 'index':
        return ''
    elif re.search(pattern, path):
        return css_class

    return ''
