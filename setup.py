from setuptools import setup, find_packages
import os, os.path
import sys

DIRNAME = os.path.dirname(__file__)

# Dynamically calculate the version based on django.VERSION.
version = __import__('fsa').__version__

setup(name='fsa',
    version=version,
    description="FreeSWITCH Admin",
    long_description="Web interface from FreeSWITCH",
    keywords='freeswitch',
    author='Oleg Dolya',
    author_email='oleg.dolya@gmail.com',
    url='http://github.com/grengojbo/fsa',
    license='GPL',
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    #packages = packages,
    #data_files = data_files,
    zip_safe = False,
    # install_requires=[
    #     'Django>=1.1',
    #     'django-extensions',
    #     'BeautifulSoup',
    #     #'userprofile',
    # ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Topic :: Office/Business',
    ],
    scripts=['scripts/fsa-build', 'scripts/fsa-backup', 'scripts/fsa-update'],
)
