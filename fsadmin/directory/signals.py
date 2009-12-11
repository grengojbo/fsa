# -*- coding: UTF-8 -*- 
"""
signals.py

Created by jbo on 2009-07-24.
Copyright (c) 2009 __MyCompanyName__. All rights reserved.
"""

from django.dispatch import Signal
import logging
l = logging.getLogger('fsadmin.directory.signals')

__author__ = '$Author:$'
__revision__ = '$Revision:$'

endpoint_signal = Signal(providing_args=['user', 'endpoint'])
create_endpoint_signal = Signal(providing_args=['user', 'endpoint'])