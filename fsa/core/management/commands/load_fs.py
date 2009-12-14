# -*- mode: python; coding: utf-8; -*-
from django.core.management.base import NoArgsCommand
from django.core.management import call_command

class Command(NoArgsCommand):
    help = "Load FSadmin default data."
    
    def handle_noargs(self, **options):
        """Load FSadmin default data."""
        call_command('loaddata', 'context.xml', 'extension.xml', 'alias.xml', 'server.xml', 'acl.xml', 'gateway.xml', 'fsgroup.xml', 'sipprofile.xml', interactive=True)
