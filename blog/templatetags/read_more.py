# -*- coding: utf-8 -*-
from django import template


register = template.Library()


@register.filter(name='read_more', is_safe=True)
def read_more(value, arg=None, url=None):
    subs = '<a class="small" href="{}">read more...</a>'.format(arg)
    return value[::-1].replace(
        '...',
        subs[::-1],
        1
    )[::-1]
