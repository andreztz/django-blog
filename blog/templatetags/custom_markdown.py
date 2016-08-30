# -*- coding: utf-8 -*-

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(value):
    extensions = [
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'video'
    ]
    return mark_safe(markdown.markdown(
        value,
        extensions=extensions,
        safe_mode=False,
        enable_attributes=False)
    )


    #return mark_safe(markdown2.markdown(force_text(value),
       #extras=["fenced-code-blocks", "cuddled-lists", "metadata", "tables", "spoiler"]))
