# encoding: utf-8
"""
xmlrcp.py

Created by http://webnewage.org/2007/12/24/xmlrpc-put-django/

Example 
from fsa.core.xmlrcp import ServerGateway

gateway = ServerGateway( "pingback" )

@gateway.connect
def ping( source_uri, target_uri, model ):
    #...

"""

from SimpleXMLRPCServer import SimpleXMLRPCDispatcher
from django.http import HttpResponse

class ServerGateway( object ):
    def __init__( self, prefix ):
        self.prefix = prefix
        try:
            # Python 2.4
            self.dispatcher = SimpleXMLRPCDispatcher()
        except TypeError:
            # Python 2.5
            self.dispatcher = SimpleXMLRPCDispatcher(allow_none=False, encoding=None)

    def add_function(self, name, func ):
        self.dispatcher.register_function( func, ".".join( [self.prefix, name] ) )

    def connect( self, func ):
        self.add_function( func.__name__, func )
        return func

    def __call__(self, request, *args, **kwargs ):
        if kwargs:
            raise RuntimeError, "Xmlrpc server gateway cannot handle key variable argumets"

        def custom_dispatch( method, params ):
            return self.dispatcher._dispatch(method, params + tuple( args ) )

        response = HttpResponse()
        if len(request.POST):
            response.write( self.dispatcher._marshaled_dispatch( request.raw_post_data, custom_dispatch ) )
        else:
            methods = self.dispatcher.system_listMethods()

            response['Content-Type'] = 'text/plain'
            for method in methods:
                # __doc__
                help = self.dispatcher.system_methodHelp(method)
                response.write("%s:\n    %s\n\n" % (method, help))

        response['Content-Length'] = str(len(response.content))
        return response
