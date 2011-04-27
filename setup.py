#/usr/bin/env python
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

# Dynamically calculate the version based on newsroom.VERSION
version_tuple = __import__('ipfilter').VERSION
if len(version_tuple) == 3:
    version = "%d.%d_%s" % version_tuple
else:
    version = "%d.%d" % version_tuple[:2]

setup(
    name = "django-ipfilter",
    version = version,
    description = "A django application to filter ip addresses in views.",
    author = "Colin Powell",
    author_email = "colin@onecardinal.com",
    url = "http://github.com/powellc/django-ipfilter/",
    packages = find_packages(),
    package_data = {
        'ipfilter': [
            'models.py',
            'middleware.py',
            'signals.py',
            'admin.py',
        ]
    },
    zip_safe = True,
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)

