# -*- mode: python; coding: utf-8; -*-  
#from django.core.management.base import NoArgsCommand
from django.core.management.color import no_style 
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from django.utils.datastructures import SortedDict

import csv, sys
import os
import gzip
import zipfile
try:
    import bz2
    has_bz2 = True
except ImportError:
    has_bz2 = False

from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--number_start', default='2000000', dest='ns', help='Start Number'),
        make_option('--number_end', default='2999999', dest='ne', help='End Number'),
        make_option('--site', default=1, dest='si', help='site'),
        make_option('--nt', default=1, dest='nt', help='Type Number'),
    )
    help = 'Generate Number Plan ./manage.py build_endpoint --number_start=2000000 --number_end=2999999 --site=1 --nt=1'
    args = '[fixture ...]'

    def handle(self, **options):
        from django.db.models import get_apps
        from django.core import serializers
        from django.db import connection, transaction
        from django.conf import settings
        from fsa.numberplan.models import NumberPlan
        
        ns = options.get('ns','')
        ne = options.get('ne','')
        si = options.get('si',1)
        nt = options.get('nt',1)

        self.style = no_style()

        verbosity = int(options.get('verbosity', 1))
        show_traceback = options.get('traceback', False)

        # commit is a stealth option - it isn't really useful as
        # a command line option, but it can be useful when invoking
        # loaddata from within another script.
        # If commit=True, loaddata will use its own transaction;
        # if commit=False, the data load SQL will become part of
        # the transaction in place when loaddata was invoked.
        commit = options.get('commit', True)

        # Keep a count of the installed objects and fixtures
        fixture_count = 0
        object_count = 0
        models = set()


        # Get a cursor (even though we don't need one yet). This has
        # the side effect of initializing the test database (if
        # it isn't already initialized).
        cursor = connection.cursor()
    
        if commit:
            transaction.commit_unless_managed()
            transaction.enter_transaction_management()
            transaction.managed(True)

        # TODO генерируем номерной план
        objects_in_fixture = NumberPlan.objects.gen_num_plan(int(ns), int(ne), int(si), int(nt))
        label_found = True
        # If we found even one object in a fixture, we need to reset the
        # database sequences.
        if object_count > 0:
            sequence_sql = connection.ops.sequence_reset_sql(self.style, models)
            if sequence_sql:
                if verbosity > 1:
                    print "Resetting sequences"
                for line in sequence_sql:
                    cursor.execute(line)

        if commit:
            transaction.commit()
            transaction.leave_transaction_management()

        if object_count == 0:
            if verbosity > 1:
                print "No fixtures found."
        else:
            if verbosity > 0:
                print "Installed %d object(s) from %d fixture(s)" % (object_count, fixture_count)

        # Close the DB connection. This is required as a workaround for an
        # edge case in MySQL: if the same connection is used to
        # create tables, load data, and query, the query can return
        # incorrect results. See Django #7572, MySQL #37735.
        if commit:
            connection.close()

