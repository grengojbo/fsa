# -*- mode: python; coding: utf-8; -*-

from django.contrib import databrowse, admin
from django.utils.translation import ugettext_lazy as _
from fsa.gateway.models import SofiaGateway

# TODO сделать нормальное отображение шлюзов с просмотром активных шлюзов
databrowse.site.register(SofiaGateway)

admin.site.register(SofiaGateway)
