# -*- coding: utf-8 -*-
import re
from django import template


register = template.Library()


@register.filter(name='media_first', is_safe=True)
def media_first(value):

    pattern = re.compile(r'<img .*/>')

    '''
    metodo findall do obj re retorna uma
    lista com as correspondencias encontradas.
    '''
    medias = pattern.findall(value)


    if len(medias) > 0 and not value.find('img') == 4:
        img = medias[0]
        subs = '<p>' + img + '<br><br>'
        # junta tudo
        return value.replace('<p>', subs, 1)
        # encontra a primeira tag <p> e substui.
    return value
