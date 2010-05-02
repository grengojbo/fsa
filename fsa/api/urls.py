# -*- mode: python; coding: utf-8; -*-
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
import views
from fsa.api.handlers import FreeSwitchAdminHandler
#from fsb.billing.api.handlers import
from fsa.cdr.views import set_cdr
auth = HttpBasicAuthentication(realm='FreeSWITCH Admin  API')

fsa_api = Resource(handler=FreeSwitchAdminHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^get/$', views.get),
    url(r'^directory/$', views.directory),
    #url(r'^cdr/$', set_cdr),
    url(r'^cdr/', include('fsa.cdr.api.urls')),
    url(r'^numberplan/', include('fsa.numberplan.api.urls')),
    url(r'^endpoint/', include('fsa.directory.api.urls')),
    url(r'^account/', include('fsb.billing.api.urls')),
    url(r'^tariff/', include('fsb.tariff.api.urls')),
    url(r'^payment/', include('fsb.payments.api.urls')),
    url(r'^lcr/', include('fsa.lcr.api.urls')),
    #url(r'^posts/(?P<emitter_format>.+)/$', blogposts),
    #url(r'^posts\.(?P<emitter_format>.+)', blogposts, name='blogposts'),

    # automated documentation
    url(r'^$', documentation_view),
)