# -*- mode: python; coding: utf-8; -*-
from django import forms
from django.conf import settings
from fsa.directory.models import Endpoint
from django.utils.translation import ugettext_lazy as _
import logging
from django.contrib.auth.models import User
from uni_form.helpers import FormHelper, Submit, Reset
from uni_form.helpers import Layout, Fieldset, Row, HTML
log = logging.getLogger("fsb.prepaid.forms")
attrs_dict = {'class': 'required'}

__author__ = '$Author: $'
__revision__ = '$Revision: $'

# place form definition here
class EndpointForm(forms.ModelForm):
    helper = FormHelper()
    submit = Submit('save', _(u'Save'))
    helper.add_input(submit)

    def __init__(self, request, *args, **kwargs):
        super(EndpointForm, self).__init__(*args, **kwargs)
        self.user = request.user
        self.ip = request.META['REMOTE_ADDR']

    class Meta:
        model = Endpoint
        fields = ['password', 'effective_caller_id_name', 'phone_type', 'enable', 'description']
        #widgets = {
        #    'phone_typ': Textarea(attrs={'cols': 80, 'rows': 20}),
        #}
        