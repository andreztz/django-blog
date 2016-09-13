# se eu tiver medo de amar eu vo ter coragem pra que...
# -*- coding: utf-8 -*-
import re
from django import template


register = template.Library()


def make_tag(tag, size):

    tag_splited = tag.split(' ', 1)

    if tag_splited[0].endswith('img'):
        if size:
            tag_edited = ''.join(
                tag_splited[0] +
                ' class="img-responsive"' +
                'width="{}"'.format(size) +
                tag_splited[1]
            )
            return tag_edited
        else:
            tag_edited = ''.join(
                tag_splited[0] +
                ' class="img-responsive"' +
                tag_splited[1]
            )
            return tag_edited
    elif tag_splited[0].endswith('frame'):
        tag_edited = ''.join(
            '<div class="embed-responsive embed-responsive-16by9">' +
            tag_splited[0] +
            ' class="embed-responsive-item"' +
            tag_splited[1] +
            '</div>'
        )
        return tag_edited


@register.filter(name='media_responsive', is_safe=True)
def media_responsive(value, size=None):
    pattern = re.compile(r'<img .*/>|<iframe .*></iframe>')
    medias = pattern.findall(value)

    new_value = ''

    if len(medias) > 0:
        for tag in medias:
            tag_edited = make_tag(tag, size)
            new_value = pattern.sub(tag_edited, value)
        return new_value
    return value
