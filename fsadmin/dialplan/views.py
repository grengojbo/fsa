# -*- qa: UTF-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from fsadmin.dialplan.models import Context
from django.views.generic.list_detail import object_list
from lib.decorators import render_to
from django.shortcuts import get_object_or_404

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# Create your views here.

@render_to('dialplan/dialplan.html')
def get(request):
    """ 
    reguest -- 
    """
    return {'context':''}

