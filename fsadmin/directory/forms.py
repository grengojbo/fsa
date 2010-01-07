# -*- mode: python; coding: utf-8; -*-
from django import forms
from django.conf import settings
from fsadmin.directory.models import Endpoint
from django.utils.translation import ugettext_lazy as _

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place form definition here
class EndpointForm(forms.ModelForm):
    
    class Meta:
        model = Endpoint
        fields = ['phone_type', 'password', 'effective_caller_id_name', 'description']
        