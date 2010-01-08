# -*- mode: python; coding: utf-8; -*- 
"""
signals.py

Created by jbo on 2009-07-24.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

import django.dispatch
import logging
l = logging.getLogger('fsa.directory.signals')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

endpoint_signal = django.dispatch.Signal(providing_args=['user', 'endpoint'])
create_endpoint_signal = django.dispatch.Signal(providing_args=['user', 'endpoint'])