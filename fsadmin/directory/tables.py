# -*- mode: python; coding: utf-8; -*-
import django_tables as tables
from fsadmin.directory.models import Endpoint
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class EndpointTable(tables.ModelTable):
    id = tables.Column(sortable=False, visible=False)
    uid = tables.Column(name="uid", data="uid", verbose_name="Номер")
    phone_type = tables.Column(name="phone_type", data='phone_type', verbose_name="Тип")
    password = tables.Column(name="password", data="password", verbose_name="Пароль", sortable=False)
    class Meta:
        model = Endpoint
        exclude = ['accountcode', 'user_context', 'effective_caller_id_name', 'enable', 'is_registered', 'last_registered', 'description']