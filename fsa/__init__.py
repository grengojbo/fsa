# -*- mode: python; coding: utf-8; -*-
import logging

l = logging.getLogger('fsa')
VERSION = (0, 4, 0)
            
# Dynamically calculate the version based on VERSION tuple
if len(VERSION)>2 and VERSION[2] is not None:
    str_version = "%d.%d_%s" % VERSION[:3]
else:
    str_version = "%d.%d" % VERSION[:2]

def get_version():
    "Returns the version as a human-format string."
    hg_rev='hg-unknown'
    v = '.'.join([str(i) for i in VERSION[:-1]])
    if VERSION[-1]:
        try:
            import os
            from mercurial import ui, hg
            dir = os.path.dirname(__file__)
            hg_dir = os.path.normpath(os.path.join(dir,"../"))
            repo = hg.repository(ui.ui(), hg_dir)
            c = repo['tip']
            v = "%s.%s.%s" % (v, c.rev(), c.hex()[0:12])
        except Exception, e:
            l.error('get_version()! %s' % e)
            v = '%s.%s' % (v, VERSION[-1])
    return v
    
__version__ = get_version()