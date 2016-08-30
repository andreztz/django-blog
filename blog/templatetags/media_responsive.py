# -*- coding: utf-8 -*-
import re
from django import template


register = template.Library()


@register.filter(name='media_responsive', is_safe=True)
def media_responsive(value, size=None):
    pattern = re.compile(r'<img .*/>|<iframe .*></iframe>')
    medias = pattern.findall(value)
    new_value = ''

    if len(medias) > 0:
        for tag in medias:

            tag_splited = tag.split(' ', 1)

            if tag_splited[0].endswith('img'):
                if size:
                    tag_edited = ''.join(
                        tag_splited[0] +
                        ' class="img-responsive"' +
                        'width="{}"'.format(size) +
                        tag_splited[1]
                    )
                else:
                    tag_edited = ''.join(
                        tag_splited[0] +
                        ' class="img-responsive"' +
                        tag_splited[1]
                    )

            elif tag_splited[0].endswith('frame'):
                tag_edited = ''.join(
                    '<div class="embed-responsive embed-responsive-16by9">' +
                    tag_splited[0] +
                    ' class="embed-responsive-item"' +
                    tag_splited[1] +
                    '</div>'
                )

            if new_value == '':
                new_value = value.replace(tag, tag_edited)
            else:
                new_value = new_value.replace(tag, tag_edited)
        return new_value
    return value
