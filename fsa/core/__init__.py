# -*- mode: python; coding: utf-8; -*- 
from django.conf import settings


class ApplicationChecker(object):
    "Checks if application is enabled"
    def __getattr__(self, attr):
        return attr in settings.INSTALLED_APPS
appcheck = ApplicationChecker()

def is_app(name):
    """Checks if application is enabled
    
    Example:
    from fsa.core import is_app 
    
    if is_app('fsadmin.testapp'):
        from fsadmin.testapp import views
    """
    return name in settings.INSTALLED_APPS
