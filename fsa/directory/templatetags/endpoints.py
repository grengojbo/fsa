# -*- mode: python; coding: utf-8; -*- 
"""
endpoints.py

Created by jbo on 2009-07-28.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from django import template
from fsa.directory.models import Endpoint, FSGroup, SipRegistration
import logging

l = logging.getLogger('fsa.directory.views')

register = template.Library()
#<a href="{% url directory_edit object_id=endpoint.pk %}">

@register.inclusion_tag('directory/endpoints.html', takes_context=True)
def endpoints(context):
    """docstring for endpoints"""
    e = Endpoint.objects.filter(accountcode = context['user'], enable=True)
    return {
        #'STATIC_URL': context['STATIC_URL'],
        #'request': context['request'],
        'e': e,
        'settings': context['settings'],
    }