# -*- coding: utf-8 -*-
import re
from django import template


register = template.Library()


# def make_tag(tag, size):

#     tag_splited = tag.split(" ", 1)

#     if tag_splited[0].endswith("img"):
#         if size:
#             tag_edited = "".join(
#                 tag_splited[0]
#                 + ' class="img-responsive"'
#                 + 'width="{}"'.format(size)
#                 + tag_splited[1]
#             )
#             return tag_edited
#         else:
#             tag_edited = "".join(
#                 tag_splited[0] + ' class="img-responsive"' + tag_splited[1]
#             )
#             return tag_edited
#     elif tag_splited[0].endswith("frame"):
#         tag_edited = "".join(
#             '<div class="embed-responsive embed-responsive-16by9">'
#             + tag_splited[0]
#             + ' class="embed-responsive-item"'
#             + tag_splited[1]
#             + "</div>"
#         )
#         return tag_edited


# @register.filter(name="media_responsive", is_safe=True)
# def media_responsive(value, size=400):
#     pattern = re.compile(r"<iframe .*></iframe>|<img .*/>")
#     medias = pattern.findall(value)

#     new_value = None
#     new_tags = []
#     if medias:
#         for tag in medias:
#             new_tags.append(make_tag(tag, size))
#     if new_tags:
#         for tag in new_tags:
#             new_value = pattern.sub(tag, value)
#         return new_value
#     return value


@register.filter(name="media_responsive", is_safe=True)
def media_responsive(value, size=400):

    return value
