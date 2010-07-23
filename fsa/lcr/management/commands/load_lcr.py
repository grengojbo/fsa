# -*- mode: python; coding: utf-8; -*-  
#from django.core.management.base import NoArgsCommand
from django.core.management.color import no_style 
from django.core.exceptions import ImproperlyConfigured
from django.core.management.base import BaseCommand, CommandError
from django.core import serializers
from django.utils.datastructures import SortedDict 
from fsa.core.utils import CsvData
from fsa.server.models import CsvBase
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
import csv, sys
import os
import gzip
import zipfile
import logging
log = logging.getLogger('fsa.lcr.management.load_lcr')
try:
    import bz2
    has_bz2 = True
except ImportError:
    has_bz2 = False

from optparse import make_option

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--gw', default=1, dest='gw', help='Gateway ID'),
        make_option('--site', default=1, dest='site', help='Site ID'),
        make_option('--format_csv', default=1, dest='format_csv', help='Format csv file'),
    )
    help = 'Load Lcr data ./manage.py load_lcr --gw=3 --site=1 --format_csv=1 /fsa/lcr/fixtures/test-lcr.csv'
    args = '[fixture ...]'

    def handle(self, fixture_labels, **options):
        from django.db.models import get_apps
        from django.core import serializers
        from django.db import connection, transaction
        from django.conf import settings
        from fsa.lcr.models import Lcr
        from fsa.gateway.models import SofiaGateway
        from currency.money import Money
        from currency.models import Currency
        from django.contrib.sites.models import RequestSite
        from django.contrib.sites.models import Site

        gw = options.get('gw',1)
        site = options.get('site',1)
        format_csv = options.get('format_csv',1)

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

        humanize = lambda dirname: dirname and "'%s'" % dirname or 'absolute path'

        # Get a cursor (even though we don't need one yet). This has
        # the side effect of initializing the test database (if
        # it isn't already initialized).
        cursor = connection.cursor()

        if commit:
            transaction.commit_unless_managed()
            transaction.enter_transaction_management()
            transaction.managed(True)

        class SingleZipReader(zipfile.ZipFile):
            def __init__(self, *args, **kwargs):
                zipfile.ZipFile.__init__(self, *args, **kwargs)
                if settings.DEBUG:
                    assert len(self.namelist()) == 1, "Zip-compressed fixtures must contain only one file."
            def read(self):
                return zipfile.ZipFile.read(self, self.namelist()[0])

        compression_types = {
            None:   file,
            'gz':   gzip.GzipFile,
            'zip':  SingleZipReader
        }
        if has_bz2:
            compression_types['bz2'] = bz2.BZ2File

        #f = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test-lcr.csv'), "rt")
        #f = open(fixture_labels, "rt")

        f = open(fixture_labels, "rt")
        try:
            gateway = SofiaGateway.objects.get(pk=gw, enabled=True)
            s = Site.objects.get(pk=site)
            #d1="delimiter=';'time_format='%d.%m.%Y 00:00'name|country_code|special_digits|rate"
            csb = CsvBase.objects.get(pk=format_csv)
            cd = CsvData(csb.val)
            log.debug(fixture_labels)
            reader = csv.reader(f, delimiter=';', dialect='excel')
            for row in reader:
                try:
                    country_list, country_code, n = cd.parse(row)
                    log.debug("country_code %s (%s)" % (country_code, country_list))
                    for country in country_list:
                        n['country_code'] = country_code
                        #digits = n['digits']
                        digits = country
                        #price = Money(n['price'], n['currency'])
                        #price = Money(n['price'], 'USD')
                        price = n['price']
                        log.debug("digits %s" % country)
                        if n['weeks'] is not None:
                            if n['weeks'] == "all":
                                n['week'] = 0;
                                objects_in_fixture = Lcr.objects.add_lcr(gateway, n, digits, price, s)
                                object_count += objects_in_fixture
                            else:
                                for i in eval(n['weeks']):
                                    n['week'] = int(i);
                                    objects_in_fixture = Lcr.objects.add_lcr(gateway, n, digits, price, s)
                                    object_count += objects_in_fixture
                except Exception, e:
                    log.error("line: %i => %s" % (cd.line_num, e))
                    pass
            label_found = True
        except Exception, e:
            log.error(e)
        finally:
            f.close()
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
