# -*- coding: UTF-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list_detail import object_list
from lib.decorators import render_to, ajax_request
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from fsa.core import is_app 
import logging

l = logging.getLogger('fsadmin.numberplan.views')

__author__ = '$Author:$'
__revision__ = '$Revision:$'
